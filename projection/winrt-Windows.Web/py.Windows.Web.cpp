// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Windows.Web.h"

namespace py::cpp::Windows::Web
{
    // ----- WebError class --------------------

    static PyObject* _new_WebError(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::Web::WebError>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::Web::WebError>::type_name);
        return nullptr;
    }

    static PyObject* WebError_GetStatus(PyObject* /*unused*/, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Web.WebError", L"GetStatus", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<int32_t>(args, 0);

                return py::convert(winrt::Windows::Web::WebError::GetStatus(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyMethodDef _methods_WebError[] = {
        { }
    };

    static PyGetSetDef _getset_WebError[] = {
        { }
    };

    static PyType_Slot _type_slots_WebError[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_WebError) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_WebError) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_WebError) },
        { }
    };

    static PyType_Spec type_spec_WebError = {
        "winrt._winrt_windows_web.WebError",
        0,
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_WebError};

    static PyGetSetDef getset_WebError_Static[] = {
        { }
    };

    static PyMethodDef methods_WebError_Static[] = {
        { "get_status", reinterpret_cast<PyCFunction>(WebError_GetStatus), METH_VARARGS, nullptr },
        { }
    };

    static PyType_Slot type_slots_WebError_Static[] = 
    {
        { Py_tp_base, reinterpret_cast<void*>(&PyType_Type) },
        { Py_tp_getset, reinterpret_cast<void*>(getset_WebError_Static) },
        { Py_tp_methods, reinterpret_cast<void*>(methods_WebError_Static) },
        { }
    };

    static PyType_Spec type_spec_WebError_Static =
    {
        "winrt._winrt_windows_web.WebError_Static",
        static_cast<int>(PyType_Type.tp_basicsize),
        static_cast<int>(PyType_Type.tp_itemsize),
        Py_TPFLAGS_DEFAULT,
        type_slots_WebError_Static
    };

    // ----- IUriToStreamResolver interface --------------------

    static PyObject* _new_IUriToStreamResolver(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::Web::IUriToStreamResolver>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::Web::IUriToStreamResolver>::type_name);
        return nullptr;
    }

    static void _dealloc_IUriToStreamResolver(py::wrapper::Windows::Web::IUriToStreamResolver* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* IUriToStreamResolver_UriToStreamAsync(py::wrapper::Windows::Web::IUriToStreamResolver* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.Web.IUriToStreamResolver", L"UriToStreamAsync", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Windows::Foundation::Uri>(args, 0);

                return py::convert(self->obj.UriToStreamAsync(param0));
            }
            catch (...)
            {
                py::to_PyErr();
                return nullptr;
            }
        }
        else
        {
            py::set_invalid_arg_count_error(arg_count);
            return nullptr;
        }
    }

    static PyObject* _assign_array_IUriToStreamResolver(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::Web::IUriToStreamResolver>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_IUriToStreamResolver(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::Web::IUriToStreamResolver>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_IUriToStreamResolver[] = {
        { "uri_to_stream_async", reinterpret_cast<PyCFunction>(IUriToStreamResolver_UriToStreamAsync), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_IUriToStreamResolver, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_IUriToStreamResolver), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_IUriToStreamResolver[] = {
        { }
    };

    static PyType_Slot _type_slots_IUriToStreamResolver[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_IUriToStreamResolver) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_IUriToStreamResolver) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_IUriToStreamResolver) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_IUriToStreamResolver) },
        { }
    };

    static PyType_Spec type_spec_IUriToStreamResolver = {
        "winrt._winrt_windows_web.IUriToStreamResolver",
        sizeof(py::wrapper::Windows::Web::IUriToStreamResolver),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_IUriToStreamResolver};

    // ----- Windows.Web Initialization --------------------

    PyDoc_STRVAR(module_doc, "Windows.Web");

    static PyModuleDef module_def = {
        PyModuleDef_HEAD_INIT,
        "_winrt_windows_web",
        module_doc,
        0,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr};
} // py::cpp::Windows::Web

PyMODINIT_FUNC PyInit__winrt_windows_web(void) noexcept
{
    using namespace py::cpp::Windows::Web;

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

    py::pyobj_handle type_WebError_Static{PyType_FromSpec(&type_spec_WebError_Static)};
    if (!type_WebError_Static)
    {
        return nullptr;
    }

    py::pytype_handle WebError_type{py::register_python_type(module.get(), &type_spec_WebError, object_bases.get(), reinterpret_cast<PyTypeObject*>(type_WebError_Static.get()))};
    if (!WebError_type)
    {
        return nullptr;
    }

    py::pytype_handle IUriToStreamResolver_type{py::register_python_type(module.get(), &type_spec_IUriToStreamResolver, object_bases.get(), nullptr)};
    if (!IUriToStreamResolver_type)
    {
        return nullptr;
    }


    return module.detach();
}
