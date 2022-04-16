package main

import (
	"fmt"
	sdk "github.com/crawlab-team/crawlab-sdk"
	"github.com/crawlab-team/crawlab-sdk/entity"
	"time"
)

func main() {
	var fields []string
	for i := 0; i < 50; i++ {
		fields = append(fields, fmt.Sprintf("field %d", i+1))
	}

	var items []entity.Result
	for i := 0; i < 5000; i++ {
		item := entity.Result{}
		for j, f := range fields {
			item[f] = fmt.Sprintf("value %d%d", i, j)
		}
		items = append(items, item)
	}
	sdk.SaveItem(items...)
	time.Sleep(5 * time.Second)
}
