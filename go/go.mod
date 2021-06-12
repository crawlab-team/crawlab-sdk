module github.com/crawlab-team/crawlab-go-sdk

go 1.15

replace (
	github.com/crawlab-team/crawlab-grpc => /Users/marvzhang/projects/crawlab-team/crawlab-grpc/dist/go
	github.com/crawlab-team/go-trace => /Users/marvzhang/projects/crawlab-team/go-trace
)

require (
	github.com/apex/log v1.9.0
	github.com/cenkalti/backoff/v4 v4.1.0
	github.com/crawlab-team/crawlab-grpc v0.0.0
	github.com/crawlab-team/go-trace v0.0.0
	github.com/stretchr/testify v1.6.1
	go.mongodb.org/mongo-driver v1.5.3
	google.golang.org/grpc v1.34.0
)
