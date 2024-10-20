// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Windows.Graphics.h"


namespace py::cpp::Windows::Graphics
{
    // ----- IGeometrySource2D interface --------------------

    static PyObject* _new_IGeometrySource2D(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::Graphics::IGeometrySource2D>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::Graphics::IGeometrySource2D>::type_name);
        return nullptr;
    }

    static void _dealloc_IGeometrySource2D(py::wrapper::Windows::Graphics::IGeometrySource2D* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_IGeometrySource2D(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::IGeometrySource2D>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_IGeometrySource2D(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Graphics::IGeometrySource2D>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IGeometrySource2D[] = {
        { "_assign_array_", _assign_array_IGeometrySource2D, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IGeometrySource2D), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IGeometrySource2D[] = {
        { }
    };

    static PyType_Slot _type_slots_IGeometrySource2D[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_IGeometrySource2D) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_IGeometrySource2D) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_IGeometrySource2D) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_IGeometrySource2D) },
        { },
    };

    static PyType_Spec type_spec_IGeometrySource2D =
    {
        "winrt._winrt_windows_graphics.IGeometrySource2D",
        sizeof(py::wrapper::Windows::Graphics::IGeometrySource2D),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IGeometrySource2D
    };

    // ----- DisplayAdapterId struct --------------------

    winrt_struct_wrapper<winrt::Windows::Graphics::DisplayAdapterId>* _new_DisplayAdapterId(PyTypeObject* subclass, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        auto self = reinterpret_cast<winrt_struct_wrapper<winrt::Windows::Graphics::DisplayAdapterId>*>(subclass->tp_alloc(subclass, 0));

        if (!self)
        {
            return nullptr;
        }

        std::construct_at(&self->obj);

        return self;
    }

    int _init_DisplayAdapterId(winrt_struct_wrapper<winrt::Windows::Graphics::DisplayAdapterId>* self, PyObject* args, PyObject* kwds) noexcept
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            self->obj = {};
            return 0;
        }

        uint32_t _LowPart{};
        int32_t _HighPart{};

        static const char* kwlist[] = {"low_part", "high_part", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "Ii", const_cast<char**>(kwlist), &_LowPart, &_HighPart))
        {
            return -1;
        }

        try
        {
            self->obj = {_LowPart, _HighPart};
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static void _dealloc_DisplayAdapterId(py::wrapper::Windows::Graphics::DisplayAdapterId* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_DisplayAdapterId(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::DisplayAdapterId>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyMethodDef _methods_DisplayAdapterId[] = {
        { "_assign_array_", _assign_array_DisplayAdapterId, METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyObject* DisplayAdapterId_get_LowPart(py::wrapper::Windows::Graphics::DisplayAdapterId* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.LowPart);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int DisplayAdapterId_set_LowPart(py::wrapper::Windows::Graphics::DisplayAdapterId* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.LowPart = py::converter<uint32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* DisplayAdapterId_get_HighPart(py::wrapper::Windows::Graphics::DisplayAdapterId* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.HighPart);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int DisplayAdapterId_set_HighPart(py::wrapper::Windows::Graphics::DisplayAdapterId* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.HighPart = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_DisplayAdapterId[] = {
        { "low_part", reinterpret_cast<getter>(DisplayAdapterId_get_LowPart), reinterpret_cast<setter>(DisplayAdapterId_set_LowPart), nullptr, nullptr },
        { "high_part", reinterpret_cast<getter>(DisplayAdapterId_get_HighPart), reinterpret_cast<setter>(DisplayAdapterId_set_HighPart), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_DisplayAdapterId[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_DisplayAdapterId) },
        { Py_tp_init, reinterpret_cast<void*>(_init_DisplayAdapterId) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_DisplayAdapterId) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_DisplayAdapterId) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_DisplayAdapterId) },
        { },
    };

    static PyType_Spec type_spec_DisplayAdapterId =
    {
        "winrt._winrt_windows_graphics.DisplayAdapterId",
        sizeof(py::wrapper::Windows::Graphics::DisplayAdapterId),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_DisplayAdapterId
    };

    // ----- DisplayId struct --------------------

    winrt_struct_wrapper<winrt::Windows::Graphics::DisplayId>* _new_DisplayId(PyTypeObject* subclass, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        auto self = reinterpret_cast<winrt_struct_wrapper<winrt::Windows::Graphics::DisplayId>*>(subclass->tp_alloc(subclass, 0));

        if (!self)
        {
            return nullptr;
        }

        std::construct_at(&self->obj);

        return self;
    }

    int _init_DisplayId(winrt_struct_wrapper<winrt::Windows::Graphics::DisplayId>* self, PyObject* args, PyObject* kwds) noexcept
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            self->obj = {};
            return 0;
        }

        uint64_t _Value{};

        static const char* kwlist[] = {"value", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "K", const_cast<char**>(kwlist), &_Value))
        {
            return -1;
        }

        try
        {
            self->obj = {_Value};
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static void _dealloc_DisplayId(py::wrapper::Windows::Graphics::DisplayId* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_DisplayId(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::DisplayId>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyMethodDef _methods_DisplayId[] = {
        { "_assign_array_", _assign_array_DisplayId, METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyObject* DisplayId_get_Value(py::wrapper::Windows::Graphics::DisplayId* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Value);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int DisplayId_set_Value(py::wrapper::Windows::Graphics::DisplayId* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Value = py::converter<uint64_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_DisplayId[] = {
        { "value", reinterpret_cast<getter>(DisplayId_get_Value), reinterpret_cast<setter>(DisplayId_set_Value), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_DisplayId[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_DisplayId) },
        { Py_tp_init, reinterpret_cast<void*>(_init_DisplayId) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_DisplayId) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_DisplayId) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_DisplayId) },
        { },
    };

    static PyType_Spec type_spec_DisplayId =
    {
        "winrt._winrt_windows_graphics.DisplayId",
        sizeof(py::wrapper::Windows::Graphics::DisplayId),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_DisplayId
    };

    // ----- PointInt32 struct --------------------

    winrt_struct_wrapper<winrt::Windows::Graphics::PointInt32>* _new_PointInt32(PyTypeObject* subclass, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        auto self = reinterpret_cast<winrt_struct_wrapper<winrt::Windows::Graphics::PointInt32>*>(subclass->tp_alloc(subclass, 0));

        if (!self)
        {
            return nullptr;
        }

        std::construct_at(&self->obj);

        return self;
    }

    int _init_PointInt32(winrt_struct_wrapper<winrt::Windows::Graphics::PointInt32>* self, PyObject* args, PyObject* kwds) noexcept
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            self->obj = {};
            return 0;
        }

        int32_t _X{};
        int32_t _Y{};

        static const char* kwlist[] = {"x", "y", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "ii", const_cast<char**>(kwlist), &_X, &_Y))
        {
            return -1;
        }

        try
        {
            self->obj = {_X, _Y};
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static void _dealloc_PointInt32(py::wrapper::Windows::Graphics::PointInt32* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_PointInt32(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::PointInt32>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyMethodDef _methods_PointInt32[] = {
        { "_assign_array_", _assign_array_PointInt32, METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyObject* PointInt32_get_X(py::wrapper::Windows::Graphics::PointInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.X);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PointInt32_set_X(py::wrapper::Windows::Graphics::PointInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.X = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* PointInt32_get_Y(py::wrapper::Windows::Graphics::PointInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Y);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int PointInt32_set_Y(py::wrapper::Windows::Graphics::PointInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Y = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_PointInt32[] = {
        { "x", reinterpret_cast<getter>(PointInt32_get_X), reinterpret_cast<setter>(PointInt32_set_X), nullptr, nullptr },
        { "y", reinterpret_cast<getter>(PointInt32_get_Y), reinterpret_cast<setter>(PointInt32_set_Y), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_PointInt32[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_PointInt32) },
        { Py_tp_init, reinterpret_cast<void*>(_init_PointInt32) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_PointInt32) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_PointInt32) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_PointInt32) },
        { },
    };

    static PyType_Spec type_spec_PointInt32 =
    {
        "winrt._winrt_windows_graphics.PointInt32",
        sizeof(py::wrapper::Windows::Graphics::PointInt32),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_PointInt32
    };

    // ----- RectInt32 struct --------------------

    winrt_struct_wrapper<winrt::Windows::Graphics::RectInt32>* _new_RectInt32(PyTypeObject* subclass, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        auto self = reinterpret_cast<winrt_struct_wrapper<winrt::Windows::Graphics::RectInt32>*>(subclass->tp_alloc(subclass, 0));

        if (!self)
        {
            return nullptr;
        }

        std::construct_at(&self->obj);

        return self;
    }

    int _init_RectInt32(winrt_struct_wrapper<winrt::Windows::Graphics::RectInt32>* self, PyObject* args, PyObject* kwds) noexcept
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            self->obj = {};
            return 0;
        }

        int32_t _X{};
        int32_t _Y{};
        int32_t _Width{};
        int32_t _Height{};

        static const char* kwlist[] = {"x", "y", "width", "height", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "iiii", const_cast<char**>(kwlist), &_X, &_Y, &_Width, &_Height))
        {
            return -1;
        }

        try
        {
            self->obj = {_X, _Y, _Width, _Height};
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static void _dealloc_RectInt32(py::wrapper::Windows::Graphics::RectInt32* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_RectInt32(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::RectInt32>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyMethodDef _methods_RectInt32[] = {
        { "_assign_array_", _assign_array_RectInt32, METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyObject* RectInt32_get_X(py::wrapper::Windows::Graphics::RectInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.X);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int RectInt32_set_X(py::wrapper::Windows::Graphics::RectInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.X = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* RectInt32_get_Y(py::wrapper::Windows::Graphics::RectInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Y);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int RectInt32_set_Y(py::wrapper::Windows::Graphics::RectInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Y = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* RectInt32_get_Width(py::wrapper::Windows::Graphics::RectInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Width);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int RectInt32_set_Width(py::wrapper::Windows::Graphics::RectInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Width = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* RectInt32_get_Height(py::wrapper::Windows::Graphics::RectInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Height);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int RectInt32_set_Height(py::wrapper::Windows::Graphics::RectInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Height = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_RectInt32[] = {
        { "x", reinterpret_cast<getter>(RectInt32_get_X), reinterpret_cast<setter>(RectInt32_set_X), nullptr, nullptr },
        { "y", reinterpret_cast<getter>(RectInt32_get_Y), reinterpret_cast<setter>(RectInt32_set_Y), nullptr, nullptr },
        { "width", reinterpret_cast<getter>(RectInt32_get_Width), reinterpret_cast<setter>(RectInt32_set_Width), nullptr, nullptr },
        { "height", reinterpret_cast<getter>(RectInt32_get_Height), reinterpret_cast<setter>(RectInt32_set_Height), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_RectInt32[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_RectInt32) },
        { Py_tp_init, reinterpret_cast<void*>(_init_RectInt32) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_RectInt32) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_RectInt32) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_RectInt32) },
        { },
    };

    static PyType_Spec type_spec_RectInt32 =
    {
        "winrt._winrt_windows_graphics.RectInt32",
        sizeof(py::wrapper::Windows::Graphics::RectInt32),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_RectInt32
    };

    // ----- SizeInt32 struct --------------------

    winrt_struct_wrapper<winrt::Windows::Graphics::SizeInt32>* _new_SizeInt32(PyTypeObject* subclass, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        auto self = reinterpret_cast<winrt_struct_wrapper<winrt::Windows::Graphics::SizeInt32>*>(subclass->tp_alloc(subclass, 0));

        if (!self)
        {
            return nullptr;
        }

        std::construct_at(&self->obj);

        return self;
    }

    int _init_SizeInt32(winrt_struct_wrapper<winrt::Windows::Graphics::SizeInt32>* self, PyObject* args, PyObject* kwds) noexcept
    {
        auto tuple_size = PyTuple_Size(args);

        if ((tuple_size == 0) && (kwds == nullptr))
        {
            self->obj = {};
            return 0;
        }

        int32_t _Width{};
        int32_t _Height{};

        static const char* kwlist[] = {"width", "height", nullptr};
        if (!PyArg_ParseTupleAndKeywords(args, kwds, "ii", const_cast<char**>(kwlist), &_Width, &_Height))
        {
            return -1;
        }

        try
        {
            self->obj = {_Width, _Height};
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static void _dealloc_SizeInt32(py::wrapper::Windows::Graphics::SizeInt32* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* _assign_array_SizeInt32(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Graphics::SizeInt32>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyMethodDef _methods_SizeInt32[] = {
        { "_assign_array_", _assign_array_SizeInt32, METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyObject* SizeInt32_get_Width(py::wrapper::Windows::Graphics::SizeInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Width);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SizeInt32_set_Width(py::wrapper::Windows::Graphics::SizeInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Width = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyObject* SizeInt32_get_Height(py::wrapper::Windows::Graphics::SizeInt32* self, void* /*unused*/) noexcept
    {
        try
        {
            return py::convert(self->obj.Height);
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static int SizeInt32_set_Height(py::wrapper::Windows::Graphics::SizeInt32* self, PyObject* arg, void* /*unused*/) noexcept
    {
        if (arg == nullptr)
        {
            PyErr_SetString(PyExc_AttributeError, "can't delete attribute");
            return -1;
        }

        try
        {
            self->obj.Height = py::converter<int32_t>::convert_to(arg);
            return 0;
        }
        catch (...)
        {
            py::to_PyErr();
            return -1;
        }
    }

    static PyGetSetDef _getset_SizeInt32[] = {
        { "width", reinterpret_cast<getter>(SizeInt32_get_Width), reinterpret_cast<setter>(SizeInt32_set_Width), nullptr, nullptr },
        { "height", reinterpret_cast<getter>(SizeInt32_get_Height), reinterpret_cast<setter>(SizeInt32_set_Height), nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SizeInt32[] = 
    {
        { Py_tp_new, reinterpret_cast<void*>(_new_SizeInt32) },
        { Py_tp_init, reinterpret_cast<void*>(_init_SizeInt32) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_SizeInt32) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_SizeInt32) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_SizeInt32) },
        { },
    };

    static PyType_Spec type_spec_SizeInt32 =
    {
        "winrt._winrt_windows_graphics.SizeInt32",
        sizeof(py::wrapper::Windows::Graphics::SizeInt32),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SizeInt32
    };

    // ----- Windows.Graphics Initialization --------------------
    PyDoc_STRVAR(module_doc, "Windows::Graphics");


    static PyModuleDef module_def
        = {PyModuleDef_HEAD_INIT,
           "_winrt_windows_graphics",
           module_doc,
           0,
           nullptr,
           nullptr,
           nullptr,
           nullptr,
           nullptr};

} // py::cpp::Windows::Graphics

PyMODINIT_FUNC PyInit__winrt_windows_graphics(void) noexcept
{
    using namespace py::cpp::Windows::Graphics;

    if (py::import_winrt_runtime() == -1)
    {
        return nullptr;
    }

    py::pyobj_handle module{PyModule_Create(&module_def)};

    if (!module)
    {
        return nullptr;
    }

    auto object_type = py::get_object_type();
    if (!object_type)
    {
        return nullptr;
    }

    py::pyobj_handle object_bases{PyTuple_Pack(1, object_type)};

    if (!object_bases)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_IGeometrySource2D, object_bases.get(), nullptr) == -1)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_DisplayAdapterId, nullptr, nullptr) == -1)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_DisplayId, nullptr, nullptr) == -1)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_PointInt32, nullptr, nullptr) == -1)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_RectInt32, nullptr, nullptr) == -1)
    {
        return nullptr;
    }

    if (py::register_python_type(module.get(), &type_spec_SizeInt32, nullptr, nullptr) == -1)
    {
        return nullptr;
    }


    return module.detach();
}
