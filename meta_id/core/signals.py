# -*- coding: utf-8 -*-

from django import dispatch

remove_portfolio_file = dispatch.Signal(providing_args=["instance"])
remove_portfolio_folder = dispatch.Signal(providing_args=["instance"])
