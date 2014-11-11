# coding=utf-8
"""Views."""

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader

from wms_client.forms import (
    WMSForm
from wms_client.models import WMS
from wms_client.app_settings import Foo


def index(request):
    """Index page which renders a WMS map.

    :param request: A django request object.
    :type request: request

    :returns: Response will be a nice looking map page.
    :rtype: HttpResponse
    """

    context = {
        'wms': wms,
    }
    return render(request, 'wms_client/index.html', context)


