package sdk

var L = NewLogger()

func Log(s string) {
	L.Log(s)
}

func Debug(s string) {
	L.Debug(s)
}

func Info(s string) {
	L.Info(s)
}

func Warn(s string) {
	L.Warn(s)
}

func Error(s string) {
	L.Error(s)
}

func Fatal(s string) {
	L.Fatal(s)
}

func Logf(s string, i ...interface{}) {
	L.Logf(s, i...)
}

func Debugf(s string, i ...interface{}) {
	L.Debugf(s, i...)
}

func Infof(s string, i ...interface{}) {
	L.Infof(s, i...)
}

func Warnf(s string, i ...interface{}) {
	L.Warnf(s, i...)
}

func Errorf(s string, i ...interface{}) {
	L.Errorf(s, i...)
}

func Fatalf(s string, i ...interface{}) {
	L.Fatalf(s, i...)
}
