#!/bin/bash

debsecan --suite bookworm --only-fixed | wc -l | at 02:30
