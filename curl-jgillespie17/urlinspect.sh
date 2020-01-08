#!/bin/bash
echo Enter URL
read urlname
curl $urlname | grep mailto
