# Django HTTP Request Interceptor & Proxy

A powerful Django-based HTTP request interceptor and proxy service that captures, logs, and optionally forwards HTTP requests. Perfect for debugging, monitoring, API testing, and request analysis.

## 🚀 Features

- **Request Interception**: Captures all incoming HTTP requests with complete details
- **Optional Forwarding**: Forward requests to target URLs using the `X-Forward-URL` header
- **Comprehensive Logging**: Dual logging system (database + file)
- **Admin Interface**: Built-in Django admin for viewing captured requests and responses
- **Full HTTP Method Support**: Handles GET, POST, PUT, DELETE, PATCH, and all other HTTP methods
- **Client IP Tracking**: Records client IP addresses for each request
- **Response Capture**: Stores response status, headers, and body when forwarding
- **Real-time Monitoring**: Live request/response logging with timestamps

## 📋 Requirements

- Python 3.8+
- Django 5.2+
- requests library

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd django-http-interceptor
   ```

2. **Install dependencies**
   ```bash
   pip install django requests
   # or if you have a requirements.txt
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 📖 Usage

### Basic Request Capture

Send any HTTP request to the catch endpoint:

```bash
# Simple request capture
curl -X POST http://localhost:8000/proxy/catch/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello World"}'
```

### Request Forwarding

Use the `X-Forward-URL` header to forward requests to another service:

```bash
# Forward request to another API
curl -X POST http://localhost:8000/proxy/catch/ \
  -H "Content-Type: application/json" \
  -H "X-Forward-URL: https://api.example.com/endpoint" \
  -d '{"data": "test"}'
```

### Webhook Testing

Perfect for testing webhooks during development:

```bash
# Configure your webhook provider to send to:
https://yourdomain.com/proxy/catch/
```

## 🏗️ Project Structure

```
mysite/
├── proxy/
│   ├── __init__.py
│   ├── admin.py          # Admin interface configuration
│   ├── models.py         # Database models for requests/responses
│   ├── urls.py          # URL routing
│   └── views.py         # Main interceptor logic
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py
├── manage.py
└── proxy.log            # Request/response log file
```

## 📊 Database Models

### CapturedRequests
Stores all intercepted request details:

| Field | Type | Description |
|-------|------|-------------|
| `method` | TextField | HTTP method (GET, POST, etc.) |
| `headers` | JSONField | Request headers as JSON |
| `body` | TextField | Request body content |
| `forward_url` | URLField | Target URL for forwarding |
| `client_ip` | GenericIPAddressField | Client's IP address |
| `timestamp` | DateTimeField | Request timestamp |

### CapturedResponses
Stores response details when forwarding:

| Field | Type | Description |
|-------|------|-------------|
| `response_status` | IntegerField | HTTP status code |
| `response_headers` | JSONField | Response headers as JSON |
| `response_body` | TextField | Response body content |

## 🔍 Admin Interface

Access the Django admin interface to view captured requests and responses:

1. Navigate to `http://localhost:8000/admin/`
2. Log in with your superuser credentials
3. View and filter captured requests and responses

## 📝 Logging

The system provides dual logging:

### File Logging
- **Location**: `proxy.log` in project root
- **Format**: Timestamped entries with full request/response details
- **Content**: Method, IP, headers, body, response status, and more

### Database Logging
- All requests and responses are stored in the database
- Accessible via Django admin or direct database queries
- Includes timestamps for historical analysis

## 🔧 Configuration

### CSRF Protection
The interceptor is configured with `@csrf_exempt` to accept requests from external sources without CSRF tokens.

### Headers Processing
- Headers are normalized to lowercase for consistency
- All headers are preserved and logged
- Special handling for `X-Forward-URL` header

## 🚀 Use Cases

- **API Development**: Test and debug API endpoints
- **Webhook Testing**: Receive and analyze webhook payloads
- **Request Monitoring**: Monitor incoming requests to your services
- **Proxy Services**: Forward requests with logging capabilities
- **Security Analysis**: Analyze request patterns and headers
- **Integration Testing**: Test third-party API integrations

## 🛡️ Security Considerations

- The service accepts requests without CSRF protection
- Consider implementing authentication for production use
- Be cautious when forwarding requests to external services
- Monitor log files for sensitive data
- Consider request rate limiting for production deployments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🆘 Support

If you encounter any issues or have questions:

1. Check the `proxy.log` file for detailed request/response information
2. Use the Django admin interface to inspect captured data
3. Enable Django debug mode for detailed error messages

---

**Made with ❤️ using Django**
