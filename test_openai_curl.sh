#!/bin/bash

# OpenAI API Test Script using curl
# This script tests the OpenAI API connectivity and basic functionality.

echo "🔍 Testing OpenAI API Connectivity with curl..."
echo "=================================================="

# Check if API key is provided
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY environment variable not set!"
    echo "Please set your OpenAI API key:"
    echo "export OPENAI_API_KEY='your-api-key-here'"
    exit 1
fi

# Check API key format
if [[ ! "$OPENAI_API_KEY" =~ ^sk- ]]; then
    echo "❌ Invalid API key format! Should start with 'sk-'"
    exit 1
fi

echo "✅ API key found: ${OPENAI_API_KEY:0:10}..."
echo ""

# Test 1: Simple API call to check authentication
echo "1. Testing API Authentication..."

response=$(curl -s -w "%{http_code}" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Hello! Please respond with \"API is working\" if you can see this message."}
        ],
        "max_tokens": 50
    }' \
    https://api.openai.com/v1/chat/completions)

http_code="${response: -3}"
response_body="${response%???}"

if [ "$http_code" = "200" ]; then
    echo "✅ Authentication successful!"
    echo "Response: $(echo "$response_body" | jq -r '.choices[0].message.content')"
else
    echo "❌ Authentication failed! Status code: $http_code"
    echo "Error: $response_body"
    exit 1
fi

echo ""

# Test 2: Test GPT-4 API (used in your workflow)
echo "2. Testing GPT-4 API..."

response=$(curl -s -w "%{http_code}" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": "Say \"GPT-4 is working\" in one sentence."}
        ],
        "max_tokens": 50,
        "temperature": 0.3
    }' \
    https://api.openai.com/v1/chat/completions)

http_code="${response: -3}"
response_body="${response%???}"

if [ "$http_code" = "200" ]; then
    echo "✅ GPT-4 API working!"
    echo "Response: $(echo "$response_body" | jq -r '.choices[0].message.content')"
else
    echo "❌ GPT-4 API failed! Status code: $http_code"
    echo "Error: $response_body"
    exit 1
fi

echo ""

# Test 3: Test DALL-E API
echo "3. Testing DALL-E API..."

response=$(curl -s -w "%{http_code}" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "dall-e-3",
        "prompt": "A simple blue circle on a white background",
        "n": 1,
        "size": "1024x1024",
        "response_format": "url"
    }' \
    https://api.openai.com/v1/images/generations)

http_code="${response: -3}"
response_body="${response%???}"

if [ "$http_code" = "200" ]; then
    echo "✅ DALL-E API working!"
    echo "Image URL: $(echo "$response_body" | jq -r '.data[0].url')"
else
    echo "❌ DALL-E API failed! Status code: $http_code"
    echo "Error: $response_body"
    exit 1
fi

echo ""
echo "=================================================="
echo "🎉 All OpenAI API tests passed!"
echo "Test completed at: $(date)" 