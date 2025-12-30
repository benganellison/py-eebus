from __future__ import annotations
from typing import Any, Type, Dict, List, Optional, Callable
from spine.type_registry import TypeRegistry
from spine import array_2_dict

def spine_type(fq_name: str, is_value_type: bool = False, no_attrib_name: bool = False):
    """
    Decorator to register SPINE types and set metadata flags.
    """
    def decorator(cls):
        cls._IS_VALUE_TYPE = is_value_type
        cls._NO_ATTRIB_NAME = no_attrib_name
        TypeRegistry.register(fq_name, cls)
        return cls
    return decorator

class SpineBase:
    """
    Base class for all SPINE types to reduce code duplication.
    Utilizes _MEMBER_INFO metadata for generic operations.
    """
    
    # _MEMBER_INFO is expected to be a list of dicts:
    # [
    #     {
    #         "name": "python_attr_name",
    #         "xml_name": "XmlName",
    #         "type": "ns_p:DataType",
    #         "is_array": False,
    #         "is_optional": True,
    #         "class_check": "int" | "str" | "bool" | "float" | "complex"
    #     },
    #     ...
    # ]
    _MEMBER_INFO: List[Dict[str, Any]] = []

    def __init__(self, **kwargs):
        for member in self._MEMBER_INFO:
            name = member["name"]
            value = kwargs.get(name)
            
            # Set the value
            setattr(self, name, value)
            
            # Type validation
            if not TypeRegistry.check_type(
                value, 
                member["type"], 
                is_optional=member["is_optional"], 
                is_array=member["is_array"]
            ):
                raise TypeError(f"{name} is not of type {member['type']}")

    def get_data(self) -> Any:
        # Check if this is a "value" type (single member, no attrib name)
        if hasattr(self, "_IS_VALUE_TYPE") and getattr(self, "_IS_VALUE_TYPE"):
            if not self._MEMBER_INFO:
                return None
            return getattr(self, self._MEMBER_INFO[0]["name"])

        # Check if this is a "no attrib name" type (flat data)
        if hasattr(self, "_NO_ATTRIB_NAME") and getattr(self, "_NO_ATTRIB_NAME"):
            if not self._MEMBER_INFO:
                return []
            return getattr(self, self._MEMBER_INFO[0]["name"])

        msg_data = []
        for member in self._MEMBER_INFO:
            value = getattr(self, member["name"])
            if value is not None:
                xml_name = member["xml_name"]
                
                if member["is_array"]:
                    # Assume array elements have get_data if they are complex
                    data_val = [x.get_data() if hasattr(x, 'get_data') else x for x in value]
                else:
                    data_val = value.get_data() if hasattr(value, 'get_data') else value
                
                msg_data.append({xml_name: data_val})
        
        return msg_data

    def __str__(self) -> str:
        result_parts = []
        for member in self._MEMBER_INFO:
            value = getattr(self, member["name"])
            if value is not None:
                if member["is_array"]:
                    val_str = ", ".join(str(x) for x in value)
                else:
                    val_str = str(value)
                
                # If no attrib name, just show the value
                if hasattr(self, "_NO_ATTRIB_NAME") and getattr(self, "_NO_ATTRIB_NAME"):
                    result_parts.append(val_str)
                else:
                    result_parts.append(f"{member['xml_name']}: {val_str}")
        
        return ", ".join(result_parts)

    @classmethod
    def from_data(cls, data: Any) -> SpineBase:
        data_dict = None
        if isinstance(data, list):
            data_dict = array_2_dict(data)
        elif isinstance(data, dict):
            data_dict = data
        elif isinstance(data, tuple) and len(data) > 0 and isinstance(data[0], dict):
            data_dict = data[0]

        if data_dict is not None:
            kwargs = {}
            for member in cls._MEMBER_INFO:
                name = member["name"]
                xml_name = member["xml_name"]
                raw_val = data_dict.get(xml_name)
                
                if raw_val is None:
                    kwargs[name] = None
                    continue
                
                if member["is_array"]:
                    kwargs[name] = [TypeRegistry.from_data(member["type"], x) for x in raw_val]
                elif member["class_check"] not in ['int', 'str', 'bool', 'float', '']:
                    kwargs[name] = TypeRegistry.from_data(member["type"], raw_val)
                else:
                    kwargs[name] = raw_val
            
            return cls(**kwargs)
        
        # Fallback for simple values
        if data and not isinstance(data, tuple) and len(cls._MEMBER_INFO) == 1:
             return cls(**{cls._MEMBER_INFO[0]["name"]: data})
             
        return cls()
