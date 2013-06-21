Based on https://bitbucket.org/RafRaf/django-poll-system

Django-poll-system


Requirements

Django 1.3, 1.4 or 1.5
JQuery (There are some problems with animation in older versions.) 

Installation

1. Install the package into your ecosystem
    >> easy_install django_poll_system
    or
    >> pip install django_poll_system


2. Add it to your INSTALLED_APPS (in settings.py). Example:

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.staticfiles',
'django.contrib.admin',
'django.contrib.admindocs',

'poll',
)


3. Add the poll's url to your urls.py.

...

urlpatterns = patterns('',
    ...

    url(r'^poll/', include('poll.urls')),
)


4. Your TEMPLATE_CONTEXT_PROCESSORS (in settings.py) should look like this:

TEMPLATE_CONTEXT_PROCESSORS = (
    # Uncomment for Django 1.3
    #'django.core.context_processors.auth',
    # Uncomment for Django 1.4 or 1.5
    #'django.contrib.auth.context_processors.auth',
   	'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.middleware.csrf.CsrfViewMiddleware',
) 


5. Run "syncdb" command:
   >> python manage.py syncdb


6. Create some queues and polls through the admin panel.


7. Insert the component into your page using a queue title. Use the code snippet below to understand how to do that.  

{% load polls_tags %}
<html>
	<head>
		<title>Test page</title>
		<script type="text/javascript" src="{{ STATIC_URL }}path_to_jquery/jquery.js"></script>
	</head>
	<body>
		<h1>Test page</h1>
		{% poll_queue "YourQueueName" %}
	</body>
</html>


================================
That's all. Example: http://polltest.pythonism.ru.
