package sdk

import (
	"github.com/crawlab-team/go-trace"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"os"
)

func GetTaskId() (id primitive.ObjectID) {
	id, err := primitive.ObjectIDFromHex(os.Getenv(TaskIdKey))
	if err != nil {
		trace.PrintError(err)
	}
	return id
}
