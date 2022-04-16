module example

go 1.15

replace (
	github.com/crawlab-team/crawlab-sdk => /Users/marvzhang/projects/crawlab-team/crawlab-sdk/go
	github.com/crawlab-team/crawlab-grpc => /Users/marvzhang/projects/crawlab-team/crawlab-grpc/dist/go
	github.com/crawlab-team/go-trace => /Users/marvzhang/projects/crawlab-team/go-trace
)

require (
	github.com/crawlab-team/crawlab-sdk v0.0.1
	go.mongodb.org/mongo-driver v1.5.3
	google.golang.org/grpc v1.34.0
)
