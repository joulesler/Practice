package main

import (
	"fmt"
	"time"
)

// Channels are producer consumer not pub/sub
// <- are blocking annotations

// The actual count is increasing much faster
func sender(c chan int) {
	for i := 0; true; i++ {
		c <- i
		time.Sleep(time.Second)
	}
}

func receiver(c chan int) {
	for {
		msg := <-c
		fmt.Print(msg)
		time.Sleep(time.Second * 5)
	}
}

func main() {
	var c chan int = make(chan int)
	go sender(c)
	go receiver(c)
	time.Sleep(time.Second * 1)
	go receiver(c)
	var input string
	fmt.Scanln(&input)

}
