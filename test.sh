#!/bin/bash

# Test Script for Project Ouroboros
# Verifies that all components are working correctly

echo "🧪 PROJECT OUROBOROS - TEST SUITE"
echo "=================================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0

# Function to test endpoint
test_endpoint() {
    local name=$1
    local url=$2
    local method=${3:-GET}
    
    echo -n "Testing $name... "
    
    if [ "$method" = "GET" ]; then
        response=$(curl -s -o /dev/null -w "%{http_code}" "$url" 2>/dev/null)
    else
        response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$url" -H "Content-Type: application/json" -d '{"chaos_type":"random"}' 2>/dev/null)
    fi
    
    if [ "$response" = "200" ]; then
        echo -e "${GREEN}✅ PASS${NC} (HTTP $response)"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}❌ FAIL${NC} (HTTP $response)"
        ((TESTS_FAILED++))
    fi
}

# Check if backend is running
echo "Checking if backend is running on http://localhost:8000..."
if ! curl -s http://localhost:8000 > /dev/null 2>&1; then
    echo -e "${RED}❌ Backend is not running!${NC}"
    echo ""
    echo "Please start the backend first:"
    echo "  cd backend && python main.py"
    exit 1
fi
echo -e "${GREEN}✅ Backend is running${NC}"
echo ""

# Run API tests
echo "Running API tests..."
echo ""

test_endpoint "Health Check" "http://localhost:8000/"
test_endpoint "Status Endpoint" "http://localhost:8000/status"
test_endpoint "Logs Endpoint" "http://localhost:8000/logs"
test_endpoint "Health Endpoint" "http://localhost:8000/health"
test_endpoint "Chaos Injection" "http://localhost:8000/chaos" "POST"

echo ""
echo "=================================="
echo "Test Results:"
echo -e "${GREEN}Passed: $TESTS_PASSED${NC}"
echo -e "${RED}Failed: $TESTS_FAILED${NC}"
echo "=================================="
echo ""

# Detailed tests
echo "Running detailed checks..."
echo ""

# Check status response
echo "Fetching status details..."
status=$(curl -s http://localhost:8000/status)
generation=$(echo $status | grep -o '"generation":[0-9]*' | cut -d':' -f2)
organism_status=$(echo $status | grep -o '"status":"[^"]*"' | cut -d':' -f2 | tr -d '"')

echo "  Generation: $generation"
echo "  Status: $organism_status"
echo ""

# Check logs
echo "Fetching recent logs..."
logs=$(curl -s http://localhost:8000/logs)
log_count=$(echo $logs | grep -o '"count":[0-9]*' | cut -d':' -f2)
echo "  Log entries: $log_count"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 All tests passed!${NC}"
    echo ""
    echo "The backend is working correctly."
    echo "You can now start the frontend:"
    echo "  cd frontend && npm run dev"
    echo ""
    echo "Then visit: http://localhost:3000"
    exit 0
else
    echo -e "${RED}❌ Some tests failed${NC}"
    echo ""
    echo "Please check the backend logs for errors."
    exit 1
fi
