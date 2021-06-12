package test

import (
	"context"
	sdk "github.com/crawlab-team/crawlab-sdk"
	"github.com/crawlab-team/crawlab-sdk/interfaces"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"os"
	"testing"
)

func init() {
	var err error
	T, err = NewTest()
	if err != nil {
		panic(err)
	}
}

var T *Test

type Test struct {
	c           *mongo.Client
	db          *mongo.Database
	col         *mongo.Collection
	colDc       *mongo.Collection
	TestDbName  string
	TestColName string
	TestDcId    primitive.ObjectID
	TestDc      bson.M
	TestTaskId  primitive.ObjectID
	resultSvc   interfaces.ResultService
}

func (t *Test) Setup(t2 *testing.T) {
	if err := t.c.Connect(context.Background()); err != nil {
		panic(err)
	}
	_, err := t.c.Database(t.TestDbName).Collection("data_collections").InsertOne(context.Background(), t.TestDc)
	if err != nil {
		panic(err)
	}
	if err := os.Setenv(sdk.TaskIdKey, t.TestTaskId.Hex()); err != nil {
		panic(err)
	}
	t2.Cleanup(t.Cleanup)
}

func (t *Test) Cleanup() {
	_ = t.col.Drop(context.Background())
	_ = t.colDc.Drop(context.Background())
	_ = t.c.Disconnect(context.Background())
}

func NewTest() (t *Test, err error) {
	t = &Test{}

	t.TestDbName = "crawlab_test"
	t.TestColName = "test_results"
	t.TestDcId = primitive.NewObjectID()
	t.TestDc = bson.M{
		"_id":  t.TestDcId,
		"name": t.TestColName,
	}
	t.TestTaskId = primitive.NewObjectID()

	t.c, err = mongo.NewClient()
	if err != nil {
		return nil, err
	}
	t.db = t.c.Database(t.TestDbName)
	t.col = t.db.Collection(t.TestColName)
	t.colDc = t.db.Collection("data_collections")
	t.resultSvc = sdk.NewResultService()

	return t, nil
}
