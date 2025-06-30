#!/usr/bin/env python3
"""
OpenAI API Test Script
This script tests the OpenAI API connectivity and basic functionality.
"""

import os
import requests
import json
from datetime import datetime

def test_openai_api():
    """Test OpenAI API connectivity and basic functionality"""
    
    print("🔍 Testing OpenAI API Connectivity...")
    print("=" * 50)
    
    # Test 1: Simple API call to check authentication
    print("\n1. Testing API Authentication...")
    
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
        'Content-Type': 'application/json'
    }
    
    # Simple test payload
    test_payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Hello! Please respond with 'API is working' if you can see this message."}
        ],
        "max_tokens": 50
    }
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=test_payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Authentication successful!")
            print(f"Response: {result['choices'][0]['message']['content']}")
        else:
            print(f"❌ Authentication failed! Status code: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Connection error: {str(e)}")
        return False
    
    # Test 2: Test DALL-E API
    print("\n2. Testing DALL-E API...")
    
    dalle_payload = {
        "model": "dall-e-3",
        "prompt": "A simple blue circle on a white background",
        "n": 1,
        "size": "1024x1024",
        "response_format": "url"
    }
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/images/generations',
            headers=headers,
            json=dalle_payload,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ DALL-E API working!")
            print(f"Image URL: {result['data'][0]['url']}")
        else:
            print(f"❌ DALL-E API failed! Status code: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ DALL-E connection error: {str(e)}")
        return False
    
    # Test 3: Test GPT-4 API (used in your workflow)
    print("\n3. Testing GPT-4 API...")
    
    gpt4_payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": "Say 'GPT-4 is working' in one sentence."}
        ],
        "max_tokens": 50,
        "temperature": 0.3
    }
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=gpt4_payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ GPT-4 API working!")
            print(f"Response: {result['choices'][0]['message']['content']}")
        else:
            print(f"❌ GPT-4 API failed! Status code: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ GPT-4 connection error: {str(e)}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 All OpenAI API tests passed!")
    print(f"Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return True

def check_api_key():
    """Check if API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY environment variable not set!")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return False
    
    if not api_key.startswith("sk-"):
        print("❌ Invalid API key format! Should start with 'sk-'")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...")
    return True

if __name__ == "__main__":
    print("OpenAI API Test Script")
    print("=" * 50)
    
    if check_api_key():
        test_openai_api()
    else:
        print("\nPlease set your OpenAI API key and try again.") 