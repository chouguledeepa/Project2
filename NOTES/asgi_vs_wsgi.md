django

    project-root
        project-root
            urls.py
            settings.py
            ..
            ..


flask --app main
python manage.py runserver

127.0.0.1 (localhost)
8080

HTTP methods 


GIL (Global Interpreter Lock)


# Examples of Web Application Servers
- Apache web server (HTTP web application)
- django lightweight development server
- flask lightweight development server
- gunicorn




# WSGI
- specifications (rule, guideline)
- gunicorn


request -> web application -> response

# synchronous

batter -> oven  -> hot cake -> cool for 30 mins -> decorate


2 ovens (multiple-processes)
batter -> oven1 -> hot cake -> cool for 30 mins -> decorate
batter -> oven2 -> hot cake -> cool for 30 mins -> decorate

2 ovens (multiple-threads)
thread1    batter -> oven1 -> hot cake -> cool for 30 mins ......................
Thread2                                  batter -> oven1 -> hot cake ..............



--------------------------------------------------------------------------->
# synchronous vs asynchronous

you only have 1 thread (sync way)

batter -> oven1 -> hot cake -> cool for 30 mins -> decorate
                                                            batter -> oven1 -> hot cake -> cool for 30 mins -> decorate


you only have 1 thread (async way)

thread-1      batter -> oven1 -> hot cake -> ................
thread-1                                    batter -> oven1 -> hot cake ..............







----------------------------------------------------------------------

# IO operations
- DB calls
- Reading and writing to files
- Over the network (HTTP calls)


# asynchronous



# ASGI
- Specification for web frameworks considering Python support 
for asynchronous programming
- fastAPI


### web portal
- sign-in using `linkedin`

[profile1, profile2, profile3]