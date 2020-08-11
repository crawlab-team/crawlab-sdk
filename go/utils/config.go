package utils

import (
	"encoding/json"
	"github.com/crawlab-team/crawlab-sdk/go/entity"
	"os"
)

func GetTaskId() string {
	return os.Getenv("CRAWLAB_TASK_ID")
}

func GetIsDedup() string {
	return os.Getenv("CRAWLAB_IS_DEDUP")
}

func GetDedupField() string {
	return os.Getenv("CRAWLAB_DEDUP_FIELD")
}

func GetDedupMethod() string {
	return os.Getenv("CRAWLAB_DEDUP_METHOD")
}

func GetCollection() string {
	return os.Getenv("CRAWLAB_COLLECTION")
}

func GetDataSourceType() string {
	ds := GetDataSource()
	if ds.Type == "" {
		return "mongo"
	}
	return ds.Type
}

func GetDataSource() (ds entity.DataSource) {
	dsStr := os.Getenv("CRAWLAB_DATA_SOURCE")
	if dsStr == "" {
		return ds
	}
	if err := json.Unmarshal([]byte(dsStr), &ds); err != nil {
		return ds
	}
	return ds
}
