"""Domain errors."""


class HydroError(Exception):
    code = 2000


class UnitError(HydroError):
    code = 2001


class FitError(HydroError):
    code = 2002


class ConvergenceError(HydroError):
    code = 2003


class ValidationError(HydroError):
    code = 2004


class NotFoundError(HydroError):
    code = 2005
