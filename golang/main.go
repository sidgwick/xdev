package main

import (
	"fmt"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/adaptor"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"time"
)

// 在程序启动时创建指标，确保只创建一次
var (
	// 定义一个全局的 Prometheus CounterVec
	httpRequests = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "http_requests_total",
			Help: "Total number of HTTP requests.",
		},
		[]string{"method", "endpoint"},
	)
)

func getNewHistogram() *prometheus.HistogramVec {
	return promauto.NewHistogramVec(
		prometheus.HistogramOpts{
			Name:    "ceshi_his",
			Help:    "",
			Buckets: []float64{10, 20, 50},
		},
		[]string{"label1", "label2"},
	)
}

func main1() {
	prometheus.MustRegister(httpRequests)

	app := fiber.New(fiber.Config{
		DisableStartupMessage: false,
	})

	// 中间件，用于计数 HTTP 请求
	app.Use(func(c *fiber.Ctx) error {
		// 获取 HTTP 请求的 method 和 endpoint
		method := c.Method()
		endpoint := c.Path()

		// 如果多个请求有相同的 method 和 endpoint 标签组合，Prometheus 会认为重复并报错
		httpRequests.WithLabelValues(method, endpoint).Inc() // 错误示例：重复增加相同标签组合的计数

		// 继续处理请求
		return c.Next()
	})

	myHistogram := getNewHistogram()
	//prometheus.MustRegister(myHistogram)

	app.Get("/metrics", adaptor.HTTPHandler(promhttp.Handler()))

	startTime := time.Now()
	duration := time.Since(startTime)
	val := float64(duration.Milliseconds())

	abc := []byte{'A', 'B', 'C'}

	// 错误：每次处理请求时都创建并注册同名的指标，这会导致冲突
	app.Get("/proxy", func(ctx *fiber.Ctx) error {
		myHistogram.WithLabelValues("value1", string(abc)).Observe(val)

		ctx.Response().SetBodyRaw(abc)
		return nil
	})

	fmt.Printf("server starting at :8080\n")
	err := app.Listen("127.0.0.1:8080")
	if err != nil {
		panic(fmt.Sprintf("Failed to listen: %v", err))
	}
}
