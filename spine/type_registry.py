from __future__ import annotations
from typing import Type, Any

class TypeRegistry:
    _registry: dict[str, Type[Any]] = {}

    @classmethod
    def register(cls, fq_name: str, type_obj: Type[Any]):
        cls._registry[fq_name] = type_obj

    @classmethod
    def get_type(cls, fq_name: str) -> Type[Any] | None:
        return cls._registry.get(fq_name)

    @classmethod
    def from_data(cls, fq_name: str, data: Any) -> Any:
        type_obj = cls.get_type(fq_name)
        if type_obj and hasattr(type_obj, 'from_data'):
            return type_obj.from_data(data)
        return data

    @classmethod
    def check_type(cls, obj: Any, fq_name: str, is_optional: bool = False, is_array: bool = False) -> bool:
        if obj is None:
            return is_optional
        
        type_obj = cls.get_type(fq_name)
        if not type_obj:
            # print(f"DEBUG: check_type {fq_name} - not registered, returning True")
            return True 
            
        if is_array:
            if not isinstance(obj, list):
                # print(f"DEBUG: check_type {fq_name} - obj is not a list: {type(obj)}")
                return False
            res = all(isinstance(x, type_obj) for x in obj)
            # if not res:
            #    print(f"DEBUG: check_type {fq_name} - list elements mismatch: expected {type_obj}, got {[type(x) for x in obj]}")
            return res
        
        res = isinstance(obj, type_obj)
        if not res:
            print(f"DEBUG: check_type {fq_name} mismatch: obj={type(obj)}, expected={type_obj}, eq={type(obj) == type_obj}")
        return res
