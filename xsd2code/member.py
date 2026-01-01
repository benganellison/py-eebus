
#from xsd2code import DataType, to_snake_case
import xsd2code


class Member:

    def __init__(self, fq_member_name, data_type: xsd2code.DataType, is_optional=False, default_value=None, is_array=False):
        self._fq_member_name = fq_member_name

        self._namespace, self._member_name = fq_member_name.split(":")

        self._data_type = data_type
        self._is_optional = is_optional
        self._default_value = default_value
        self._is_array = is_array


    @property
    def member_name(self):
        return self._member_name

    @property
    def snake_case_name(self):
        return xsd2code.to_snake_case(self._member_name)


    @property
    def data_type(self):
        return self._data_type

    @property
    def class_name(self):
        if self._is_array:
            return f"list[{self._data_type.class_name}]"
        else:
            return self._data_type.class_name

    @property
    def class_check(self):
        if self._is_array:
            return f"list"
        else:
            return self._data_type.class_name

    @property
    def has_default_or_optional(self):
        return True

    @property
    def data_access_method(self):
        if self._is_array:
            return f"[d{self._data_type.data_access_method} for d in self.{self.snake_case_name}]"
        else:
            return f"self.{self.snake_case_name}{self._data_type.data_access_method}"

    @property
    def is_array(self):
        return self._is_array
    
    @property
    def is_optional(self):
        return self._is_optional
    
    @property
    def default_value(self):
        return self._default_value

    def __eq__(self, other):
        if type(self) is not type(other):
            return False

        if self._fq_member_name == other._fq_member_name and \
           self._data_type == other._data_type:
            return True

        return False

    def __str__(self):
        return self._fq_member_name

    @property
    def fq_name(self):
        return self._fq_member_name

    @property
    def metadata(self):
        # (xml_name, attr_name, type_fq_name, is_optional, is_array, access_method)
        return (
            self.member_name,
            self.snake_case_name,
            self.data_type.fq_name,
            self.is_optional,
            self.is_array,
            self.data_type.data_access_method
        )


