package main

import (
	sdk "github.com/crawlab-team/crawlab-sdk"
	"github.com/crawlab-team/crawlab-sdk/entity"
	"time"
)

func main() {
	item := entity.Result{
		"hello": "world",
	}
	sdk.SaveItem(item)
	time.Sleep(5 * time.Second)
}
