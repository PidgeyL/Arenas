#!/usr/bin/env python3
###############################################################
# Arg - Env - Ask
#
# Library to try and get variables from the system environment,
#  script arguments or interactively with the user
#
################################################################
import os
import sys

def _get_from_env(env):
    return os.getenv(env)


def _get_from_args(args):
    if not isinstance(args, list):
        args = [str(args)]
    for i, arg in enumerate(sys.argv):
        if arg in args:
            if i + 1 == len(sys.argv):
                print("No argument supplied")
                sys.exit(2)
            return sys.argv[i+1]


def _get_from_ask(ask):
    return input(ask + ': ')



def arenas_get(env, args, ask, required=True, non_interactive=False):
    # First try to get from arguments
    var = _get_from_args(args)
    if var: return var

    # If not in args, try to get from env
    var = _get_from_env(env)
    if var: return var

    # If the var is required but we cannot fetch it, exit
    if non_interactive and required:
        print("Could not obtain required variable")
        sys.exit(1)

    # Else ask, unless non-interactive
    if non_interactive:
        return None

    return _get_from_ask(ask)


