#!/bin/env python
# -*- coding: utf-8 -*-
##
# driver.py: Example of a script that calls into Q# from Python.
##
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
##

## GETTING STARTED ############################################################

# To start, simply import the qsharp module.
import qsharp

# After importing the qsharp module, Q# namespaces can be imported like any
# other Python packages.
from Microsoft.Quantum.Python import HelloQ, HelloAgain, HelloTuple

## SIMULATING FUNCTIONS AND OPERATIONS ########################################

# All Q# operations defined in any .qs file inside the same working directory
# (the Q# workspace) are automatically identified.
# You can simulate operation or function in the current workspace simply by
# calling the `simulate` method on Q# functions and operations once they've been
# imported.
r = HelloQ.simulate()
print("HelloQ result: ", r)
print("")

# If a Q# operation or function receives parameters, just include them as named
# parameters of the same simulate method.
r = HelloAgain.simulate(count=3, name="Counting")
print("HelloAgain result: ", r)
print("")

# All built-in Q# types other qubits, functions, and operations are currently
# supported, and can be passed between Python and Q#.
r = HelloTuple.simulate(count=2, tuples=[(1, "uno"), (2, "dos"), (3, "tres"), (4, "cuatro")])
print("HelloTuple result: ", r)
print("")

# On top of simulation, you can also estimate the quantum resources required
# to run an operation, including the count of primitive operations used by the
# algorithm and the number of required qubits.
# For this, invoke the `estimate_resources` method on the operation:
r = HelloAgain.estimate_resources(count=5, name="Counting")
print(r)

## ADDING PACKAGES ############################################################

# Additional Q# packages can be added from NuGet.org using the `qsharp.packages`
# object.

qsharp.packages.add("Microsoft.Quantum.Chemistry")

# To get a list of packages currently added to the Q# workspace, just iterate
# over `qsharp.packages`, for instance by making a `dict`.
print(dict(qsharp.packages))

## COMPILING ON THE FLY #######################################################

# You can also compile Q# operations on the fly from Python
# and simulate them.
# To create an operation on the fly, call the `qsharp.compile` function
# with the source for a valid Q# code snippet containing the operation
# definition.
# For example:
hello = qsharp.compile("""
    operation HelloQ() : Result {
        Message($"Hello from quantum world!");
        return Zero;
    }
""")

# if successful, `compile` returns a Q# operation that can now be simulated or traced:
r = hello.simulate()
print("First snippet: ", r)
print()

# You may call `compile` multiple times, and may refer to operations previously defined in other snippets:
call_hello = qsharp.compile("""
    operation CallHello() : Bool {
        Message("Calling HelloQ");
        if (HelloQ() == One) {
            return true;
        } else {
            return false;
        }
    }
""")
r = call_hello.simulate()
print("Second snippet: ", r)
print()

# Calling `compile` using a previous snippet id updates the corresponding definition
hello = qsharp.compile("""
    operation HelloQ() : Result {
        Message("MSG1");
        Message("MSG2");

        return One;
    }
""")
r = call_hello.simulate()
print("Revised snippet: ", r)
print()
