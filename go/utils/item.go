package utils

import (
	"fmt"
	"github.com/crawlab-team/crawlab-sdk/go/entity"
	"strings"
)

func GetItemKeys(item entity.Item) (res []string) {
	for k := range item {
		res = append(res, k)
	}
	return res
}

func GetItemValues(item entity.Item) (res []string) {
	for _, v := range item {
		res = append(res, v.(string))
	}
	return res
}

func GetItemValuesWithQuote(item entity.Item) (res []string) {
	for _, v := range item {
		res = append(res, "'"+v.(string)+"'")
	}
	return res
}

func GetItemSqlUpdateStr(item entity.Item) string {
	var arr []string
	for k, v := range item {
		arr = append(arr, fmt.Sprintf("%s = '%s'", k, v))
	}
	return strings.Join(arr, ",")
}
