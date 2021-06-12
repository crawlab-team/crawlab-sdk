package test

import (
	"context"
	"github.com/crawlab-team/crawlab-sdk/entity"
	"github.com/stretchr/testify/require"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo/options"
	"testing"
)

func TestResultService_SaveItem(t *testing.T) {
	var err error
	T.Setup(t)

	n := 1000
	for i := 0; i < n; i++ {
		item := entity.Result{
			"key": i,
		}
		T.resultSvc.SaveItem(item)
	}

	// validate
	fr, err := T.col.Find(context.Background(), nil, &options.FindOptions{
		Sort: bson.D{{"_id", 1}},
	})
	require.Nil(t, err)
	var results []entity.Result
	err = fr.All(context.Background(), &results)
	require.Nil(t, err)
	require.Len(t, results, n)
	for i, r := range results {
		v, ok := r["key"]
		require.True(t, ok)
		require.Equal(t, i, v)
	}
}
