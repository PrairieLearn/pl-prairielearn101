_OldJsonEncoder = None
_oldOrjsonDumps = None
_oldMutableMappingSubclasshook = None


class MonkeypatchWarning(UserWarning):  pass


def checkCExtension(*, warn, warn_c = False):
    import lib.frozendict as cool
    
    
    res = cool.c_ext
    
    if warn and res == warn_c:
        if warn_c:
            msg = "C Extension version, monkeypatch will be not applied"
        else:
            msg = "Pure Python version, monkeypatch will be not applied"
        
        
        import warnings
        
        
        warnings.warn(msg, MonkeypatchWarning)
    
    
    return res


def patchOrUnpatchJson(*, patch, warn = True):
    if not checkCExtension(warn = warn):
        return
    
    
    from importlib import import_module
    self = import_module(__name__)
    import frozendict as cool
    import json
    
    
    OldJsonEncoder = self._OldJsonEncoder
    FrozendictJsonEncoder = cool._getFrozendictJsonEncoder(OldJsonEncoder)
    DefaultJsonEncoder = FrozendictJsonEncoder if patch else OldJsonEncoder
    
    if DefaultJsonEncoder == None:
        default_json_encoder = None
    else:
        default_json_encoder = DefaultJsonEncoder(
            skipkeys = False,
            ensure_ascii = True,
            check_circular = True,
            allow_nan = True,
            indent = None,
            separators = None,
            default = None,
        )
    
    if patch:
        if OldJsonEncoder == None:
            self._OldJsonEncoder = json.encoder.JSONEncoder
    else:
        if OldJsonEncoder == None:
            raise ValueError(
                "Old json encoder is None " +  
                "(maybe you already unpatched json?)"
            )
        
        self._OldJsonEncoder = None
        
    
    cool.FrozendictJsonEncoder = FrozendictJsonEncoder
    
    json.JSONEncoder = DefaultJsonEncoder
    json.encoder.JSONEncoder = DefaultJsonEncoder
    json._default_encoder = default_json_encoder
    

def patchOrUnpatchOrjson(*, patch, warn = True):
    if not checkCExtension(warn = warn):
        return
    
    
    from importlib import import_module
    self = import_module(__name__)
    import orjson
    
    if self._oldOrjsonDumps == None:
        if not patch:
            raise ValueError(
                "Old orjson encoder is None " + 
                "(maybe you already unpatched orjson?)"
            )
        
        oldOrjsonDumps = orjson.dumps
    else:
        oldOrjsonDumps = self._oldOrjsonDumps
    
    
    if patch:
        from frozendict import frozendict
        
        
        def frozendictOrjsonDumps(obj, *args, **kwargs):
            if isinstance(obj, frozendict):
                obj = dict(obj)
            
            return oldOrjsonDumps(obj, *args, **kwargs)
        
        
        defaultOrjsonDumps = frozendictOrjsonDumps
        newOldOrjsonDumps = oldOrjsonDumps
    else:
        defaultOrjsonDumps = oldOrjsonDumps
        newOldOrjsonDumps = None
    
    self._oldOrjsonDumps = newOldOrjsonDumps
    orjson.dumps = defaultOrjsonDumps
    orjson.orjson.dumps = defaultOrjsonDumps


def patchOrUnpatchMutableMappingSubclasshook(*, patch, warn = True):
    warn_c = True
    
    
    if checkCExtension(warn = warn, warn_c = warn_c):
        return
    
    
    from importlib import import_module
    self = import_module(__name__)
    from collections.abc import MutableMapping
    from lib.frozendict import frozendict
    
    
    if self._oldMutableMappingSubclasshook == None:
        if not patch:
            raise ValueError(
                "Old MutableMapping subclasshook is None " + 
                "(maybe you already unpatched MutableMapping?)"
            )
        
        oldMutableMappingSubclasshook = MutableMapping.__subclasshook__
    else:
        oldMutableMappingSubclasshook = self._oldMutableMappingSubclasshook
    
    if patch:
        @classmethod
        def frozendictMutableMappingSubclasshook(
            klass, 
            subclass, 
            *args, 
            **kwargs
        ):
            if klass == MutableMapping:
                if issubclass(subclass, frozendict):
                    return False
                
                return oldMutableMappingSubclasshook(
                    subclass, 
                    *args, 
                    **kwargs
                )
            
            return NotImplemented
        
        
        defaultMutableMappingSubclasshook = frozendictMutableMappingSubclasshook
        newOldMutableMappingSubclasshook = oldMutableMappingSubclasshook
    else:
        defaultMutableMappingSubclasshook = oldMutableMappingSubclasshook
        newOldMutableMappingSubclasshook = None
    
    self._oldMutableMappingSubclasshook = newOldMutableMappingSubclasshook
    MutableMapping.__subclasshook__ = defaultMutableMappingSubclasshook
    
    try:
        MutableMapping._abc_caches_clear()
    except AttributeError:
        MutableMapping._abc_cache.discard(frozendict)
        MutableMapping._abc_negative_cache.discard(frozendict)


def patchOrUnpatchAll(*, patch, warn = True, raise_orjson = False):
    patchOrUnpatchJson(patch = patch, warn = warn)

    try:
        import orjson
    except ImportError:
        if raise_orjson:
            raise
    else:
        patchOrUnpatchOrjson(patch = patch, warn = warn)

    patchOrUnpatchMutableMappingSubclasshook(patch = patch, warn = warn)

__all__ = (
    patchOrUnpatchJson.__name__, 
    patchOrUnpatchOrjson.__name__, 
    patchOrUnpatchMutableMappingSubclasshook.__name__, 
    patchOrUnpatchAll.__name__, 
    MonkeypatchWarning.__name__, 
)
