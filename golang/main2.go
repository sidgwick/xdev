package main

import (
	"fmt"
	"github.com/spf13/cast"
	"io"
	"math/rand"
	"net/http"
	"sync"
)

func tokens() {
	rn := rand.Uint64() % 100
	rns := cast.ToString(rn)

	url := "https://v2-api-eu.native.org/swap-api-v2/v1/orderbook?chain=solana&isDebug=1"
	method := "GET"

	req, err := http.NewRequest(method, url, nil)

	if err != nil {
		fmt.Println(err)
		return
	}

	req.Header.Add("x-key", rns)
	req.Header.Add("api_key", "e6081d6efaf2426c9d7ce652c6da402d")

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer func() {
		_ = res.Body.Close()
	}()

	body, err := io.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(string(body))
}

func tokens1(host string) {
	rn := rand.Uint64() % 100
	rns := cast.ToString(rn)

	url := fmt.Sprintf("%s", host)
	method := "GET"

	req, err := http.NewRequest(method, url, nil)

	if err != nil {
		fmt.Println(err)
		return
	}

	req.Header.Add("x-key", rns)
	req.Header.Add("api_key", "e6081d6efaf2426c9d7ce652c6da402d")

	client := &http.Client{}
	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer func() {
		_ = res.Body.Close()
	}()

	body, err := io.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(string(body))
}

func main() {
	wg := &sync.WaitGroup{}

	for i := 0; i < 100; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()
			for {
				tokens1("http://127.0.0.1:8082/jupiter/rfq/abc")
				tokens1("http://127.0.0.1:8082/jupiter/rfq/def")
			}
		}()
	}

	wg.Wait()
}
