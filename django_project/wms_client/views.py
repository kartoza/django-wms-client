# coding=utf-8
"""Views."""

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader

from wms_client.models import WMSResource
from wms_client.app_settings import *


def index(request):
    """Index page which renders a WMS map.

    :param request: A django request object.
    :type request: request

    :returns: Response will be a nice looking map page.
    :rtype: HttpResponse
    """
    wms_set = WMSResource.objects.order_by('name')
    return render(
        request,
        'wms_client/index.html',
        {'wms_set': wms_set})


def map(request, slug):
    """Index page which renders a WMS map.

    :param request: A django request object.
    :type request: request

    :param slug: Slug


    :returns: Response will be a nice looking map page.
    :rtype: HttpResponse
    """

    return render(request, 'wms_client/index.html')
