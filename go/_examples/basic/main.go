package main

import (
	sdk "github.com/crawlab-team/crawlab-sdk"
	"github.com/crawlab-team/crawlab-sdk/entity"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"os"
	"time"
)

func init() {
	_ = os.Setenv(sdk.TaskIdKey, primitive.NewObjectID().Hex())
}

func main() {
	item := entity.Result{
		"hello": "world",
	}
	sdk.SaveItem(item)
	time.Sleep(5 * time.Second)
}
