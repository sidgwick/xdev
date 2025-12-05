package main

import (
	"math/big"
	"math/rand"
	"testing"

	"github.com/shopspring/decimal"
	"github.com/spf13/cast"
	"github.com/stretchr/testify/assert"
)

func exampleBigIntStringData() [][2]string {
	values := [][2]string{}
	v1 := cast.ToString(rand.Int63())
	v2 := cast.ToString(rand.Int63())
	values = append(values, [2]string{v1, v2})
	return values
}

func exampleInt64Data() [][2]int64 {
	values := [][2]int64{}

	for i := 0; i < 50000; i++ {
		v1 := rand.Int63()
		v2 := rand.Int63()
		values = append(values, [2]int64{v1, v2})
	}

	return values
}

func exampleBigIntData(int64Values [][2]int64) [][2]*big.Int {
	values := [][2]*big.Int{}

	for _, val := range int64Values {
		v1 := big.NewInt(val[0])
		v2 := big.NewInt(val[1])
		values = append(values, [2]*big.Int{v1, v2})
	}

	return values
}

func exampleDecimalData(int64Values [][2]int64) [][2]decimal.Decimal {
	result := [][2]decimal.Decimal{}

	for _, val := range int64Values {
		v1 := decimal.New(val[0], 0)
		v2 := decimal.New(val[1], 0)
		result = append(result, [2]decimal.Decimal{v1, v2})
	}

	return result
}

func exampleBigIntDataFromString(strValues [][2]string) [][2]*big.Int {
	values := [][2]*big.Int{}

	for _, val := range strValues {
		v1 := big.Int{}
		v2 := big.Int{}

		v1.SetString(val[0], 10)
		v2.SetString(val[1], 10)

		values = append(values, [2]*big.Int{&v1, &v2})
	}

	return values
}

func exampleDecimalDataFromString(strValues [][2]string) [][2]decimal.Decimal {
	result := [][2]decimal.Decimal{}

	for _, val := range strValues {
		v1, _ := decimal.NewFromString(val[0])
		v2, _ := decimal.NewFromString(val[1])
		result = append(result, [2]decimal.Decimal{v1, v2})
	}

	return result
}

func calcDecimal(vals [2]decimal.Decimal) (decimal.Decimal, decimal.Decimal, decimal.Decimal, decimal.Decimal) {
	v1 := vals[0]
	v2 := vals[1]

	va := v1.Add(v2)
	vb := v1.Sub(v2)
	vc := v1.Mul(v2)
	vd := v1.Div(v2)
	return va, vb, vc, vd
}

func calcBigInt(vals [2]*big.Int) (big.Int, big.Int, big.Int, big.Int) {
	v1 := vals[0]
	v2 := vals[1]

	var va, vb, vc, vd big.Int

	va.Add(v1, v2)
	vb.Sub(v1, v2)
	vc.Mul(v1, v2)
	vd.Div(v1, v2)

	return va, vb, vc, vd
}

func Benchmark_NewDecimalOperation(b *testing.B) {
	int64Values := exampleInt64Data()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		exampleDecimalData(int64Values)
	}
}

func Benchmark_NewBigIntOperation(b *testing.B) {
	int64Values := exampleInt64Data()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		exampleBigIntData(int64Values)
	}
}

func Benchmark_NewStringDecimalOperation(b *testing.B) {
	values := exampleBigIntStringData()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		exampleDecimalDataFromString(values)
	}
}

func Benchmark_NewStringBigIntOperation(b *testing.B) {
	values := exampleBigIntStringData()
	b.ResetTimer()

	for n := 0; n < b.N; n++ {
		exampleBigIntDataFromString(values)
	}
}

func Benchmark_DecimalOperation(b *testing.B) {
	int64Values := exampleInt64Data()
	values := exampleDecimalData(int64Values)
	b.ResetTimer() // 重置计时器，忽略初始化时间

	for n := 0; n < b.N; n++ {
		for _, vals := range values {
			// +, -, *, / 各做一次
			calcDecimal(vals)
		}
	}
}

func Benchmark_BigIntOperation(b *testing.B) {
	int64Values := exampleInt64Data()
	values := exampleBigIntData(int64Values)
	b.ResetTimer() // 重置计时器，忽略初始化时间

	for n := 0; n < b.N; n++ {
		for _, vals := range values {
			// +, -, *, / 各做一次
			calcBigInt(vals)
		}
	}
}

func Test_DecimalBigIntOperation(t *testing.T) {
	int64Values := exampleInt64Data()
	decimalValues := exampleDecimalData(int64Values)
	int64Vvalues := exampleBigIntData(int64Values)

	for k, vals := range decimalValues {
		// +, -, *, / 各做一次
		a0, b0, c0, d0 := calcDecimal(vals)
		a1, b1, c1, d1 := calcBigInt(int64Vvalues[k])

		a2 := a0.BigInt()
		b2 := b0.BigInt()
		c2 := c0.BigInt()
		d2 := d0.BigInt()

		assert.Equal(t, a2, &a1, "op add should be the same")
		assert.Equal(t, b2, &b1, "op sub should be the same")
		assert.Equal(t, c2, &c1, "op mul should be the same")
		assert.Equal(t, d2, &d1, "op div should be the same")
	}
}
