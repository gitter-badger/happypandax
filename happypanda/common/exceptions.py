"""exceptions module."""
import logging

log = logging.getLogger(__name__)
log_i = log.info
log_d = log.debug
log_w = log.warning
log_e = log.error
log_c = log.critical


class HappypandaError(RuntimeError):
    """Base Happypanda exception, all exceptions will derive from this."""

    def __init__(self, msg):
        """init func."""
        super().__init__()
        from happypanda.common.utils import eprint  # HACK: check if importing from __init__ works
        log_e(msg)
        eprint(msg)

# ## CORE ##


class CoreError(HappypandaError):
    """Base Happypanda core exception, all core exceptions will derive from this.

    Params:
        where -- where the error occured
        message -- explanation of error
    """

    def __init__(self, where, message):
        """init func."""
        super().__init__(message)
        self.where = where
        self.msg = message

        # ## PLUGINS ##


class PluginError(CoreError):
    """Base plugin exception, all plugin exceptions will derive from this.

    Params:
        name -- name of plugin
        message -- explanation of error
    """

    def __init__(self, name, message):
        """init func."""
        super().__init__("Plugin: " + name, message)


class PluginIDError(PluginError):
    """Plugin ID Error."""

    pass


class PluginNameError(PluginIDError):
    """Plugin Name Error."""

    pass


class PluginMethodError(PluginError):
    """Plugin Method Error."""

    pass


class PluginAttributeError(PluginError):
    """Plugin Attribute Error."""

    pass


class PluginHookError(PluginError):
    """Plugin Hook Error."""

    pass


class PluginHandlerError(PluginError):
    """Plugin Handler Error."""

    pass

    # ## DATABASE ##


class DatabaseError(CoreError):
    """Base database exception, all database exceptions will derive from this."""

    pass


class DatabaseInitError(CoreError):
    """Database initialization error."""

    def __init__(self, msg):
        """init func."""
        super().__init__("An error occured in the database initialization process: " + msg)

    # ## SERVER ##


class ServerError(CoreError):
    """Base server exception, all server exceptions will derive from this."""

    pass


class ClientDisconnectError(ServerError):
    """Client disconnected."""

    pass

    # ## CLIENT ##


class ClientError(ServerError):
    """Base client exception, all client exceptions will derive from this.

    Params:
        name -- name of client
        msg -- error message
    """

    def __init__(self, name, msg):
        """init func."""
        try:
            super().__init__("An error occured in client '{}':\t{} ".format(name, msg))
        except:
            super().__init__(name, "An error occured in client :\t{} ".format(msg))


class ServerDisconnectError(ClientError):
    """Server disconnected."""

    pass

    # ## ETC. ##


class XMLParseError(ClientError, ServerError):
    """XML parse error."""

    def __init__(self, xml_data, name, msg):
        """init func."""
        pass
        # TODO: init both classs. log xml_data.
