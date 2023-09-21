#!/bin/bash

lettre="$1"

find /etc -type f -name "${lettre}*" -exec file {} \;


