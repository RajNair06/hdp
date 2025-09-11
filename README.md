# Django HTTP Request Interceptor & Proxy

[![Django](https://img.shields.io/badge/Django-5.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)


A lightweight Django service for intercepting, logging, and optionally forwarding HTTP requests. Perfect for webhook testing, API debugging, and request monitoring.

## ✨ Features

- 🔍 **Capture All HTTP Methods** - GET, POST, PUT, DELETE, PATCH, etc.
- 🔄 **Optional Request Forwarding** - Forward to any URL via custom header
- 💾 **Dual Logging** - Database storage + file logging
- 🖥️ **Admin Interface** - Built-in Django admin for request analysis
- 🌐 **Client IP Tracking** - Monitor request origins
- ⚡ **Real-time Processing** - Instant request/response handling
- 🛡️ **CSRF Exempt** - Accept external requests without tokens

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 5.2+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-http-interceptor.git
   cd django-http-interceptor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create admin user (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

The service will be available at `http://localhost:8000/proxy/catch/`

## 📚 Usage

### Basic Request Interception

Send any request to capture and log it:

```bash
curl -X POST http://localhost:8000/proxy/catch/ \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

### Request Forwarding

Forward requests to another service using the `X-Forward-URL` header:

```bash
curl -X POST http://localhost:8000/proxy/catch/ \
  -H "Content-Type: application/json" \
  -H "X-Forward-URL: https://httpbin.org/post" \
  -d '{"message": "Hello World"}'
```

### Webhook Testing

Point your webhook URLs to this service for testing:

```
https://yourdomain.com/proxy/catch/
```

## 🏗️ How It Works

1. **Request Capture**: All incoming requests are intercepted at `/proxy/catch/`
2. **Data Extraction**: Method, headers, body, and client IP are captured
3. **Optional Forwarding**: If `X-Forward-URL` header is present, request is forwarded
4. **Logging**: Request and response details are saved to database and log file
5. **Response**: Returns either the forwarded response or a simple confirmation

## 📊 Data Storage

### Captured Requests Table
- HTTP method and headers
- Request body and client IP
- Forward URL (if specified)
- Timestamp

### Captured Responses Table  
- HTTP status code
- Response headers and body
- Linked to original request

## 🔍 Monitoring & Analysis

### Admin Interface
Access at `http://localhost:8000/admin/` to:
- Browse all captured requests and responses
- Filter by method, IP, timestamp
- Search through request bodies and headers

### Log File
Check `proxy.log` in the project root for detailed request/response logs.

## 💡 Use Cases

- **Webhook Development**: Test webhook integrations locally
- **API Debugging**: Monitor and analyze API calls
- **Request Forwarding**: Create a logging proxy for existing APIs
- **Security Testing**: Analyze malicious request patterns
- **Integration Testing**: Verify third-party service communications

## 🛠️ Configuration

The service works out-of-the-box, but you can customize:

- **Logging Level**: Modify `logger.setLevel()` in `views.py`
- **Log File Location**: Change `proxy.log` path in the file handler
- **Database Settings**: Standard Django database configuration

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/django-http-interceptor.git
cd django-http-interceptor
pip install -r requirements.txt  # Create this with your dependencies
python manage.py migrate
python manage.py runserver
```

## 🔒 Security Notes

- This service is designed for development and testing
- Consider authentication for production deployments
- Be cautious when forwarding to external URLs
- Monitor logs for sensitive data exposure



## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!

---

**Built with Django** 🎸