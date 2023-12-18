#!/bin/bash

url="https://xkcd.com/2862"

page=$(wget -qO- "$url")

echo "$page" | grep "meta"
