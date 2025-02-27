// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#include "py.Windows.System.Implementation.FileExplorer.h"

namespace py::cpp::Windows::System::Implementation::FileExplorer
{
    // ----- SysStorageProviderEventReceivedEventArgs class --------------------

    static PyObject* _new_SysStorageProviderEventReceivedEventArgs(PyTypeObject* type, PyObject* args, PyObject* kwds) noexcept
    {
        if (kwds != nullptr)
        {
            py::set_invalid_kwd_args_error();
            return nullptr;
        }

        auto arg_count = PyTuple_Size(args);
        if (arg_count == 1)
        {
            try
            {
                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                winrt::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs instance{param0};
                return py::wrap(instance, type);
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

    static void _dealloc_SysStorageProviderEventReceivedEventArgs(py::wrapper::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* SysStorageProviderEventReceivedEventArgs_get_Json(py::wrapper::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs* self, void* /*unused*/) noexcept
    {
        try
        {
            static std::optional<bool> is_property_present{};

            if (!is_property_present.has_value())
            {
                is_property_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsPropertyPresent(L"Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs", L"Json");
            }

            if (!is_property_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "property is not available in this version of Windows");
                return nullptr;
            }

            return py::convert(self->obj.Json());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_SysStorageProviderEventReceivedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_SysStorageProviderEventReceivedEventArgs(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_SysStorageProviderEventReceivedEventArgs[] = {
        { "_assign_array_", _assign_array_SysStorageProviderEventReceivedEventArgs, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_SysStorageProviderEventReceivedEventArgs), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_SysStorageProviderEventReceivedEventArgs[] = {
        { "json", reinterpret_cast<getter>(SysStorageProviderEventReceivedEventArgs_get_Json), nullptr, nullptr, nullptr },
        { }
    };

    static PyType_Slot _type_slots_SysStorageProviderEventReceivedEventArgs[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_SysStorageProviderEventReceivedEventArgs) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_SysStorageProviderEventReceivedEventArgs) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_SysStorageProviderEventReceivedEventArgs) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_SysStorageProviderEventReceivedEventArgs) },
        { }
    };

    static PyType_Spec type_spec_SysStorageProviderEventReceivedEventArgs = {
        "winrt._winrt_windows_system_implementation_fileexplorer.SysStorageProviderEventReceivedEventArgs",
        sizeof(py::wrapper::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_SysStorageProviderEventReceivedEventArgs};

    // ----- ISysStorageProviderEventSource interface --------------------

    static PyObject* _new_ISysStorageProviderEventSource(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource>::type_name);
        return nullptr;
    }

    static void _dealloc_ISysStorageProviderEventSource(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* ISysStorageProviderEventSource_add_EventReceived(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource* self, PyObject* arg) noexcept
    {
        try
        {
            static std::optional<bool> is_event_present{};

            if (!is_event_present.has_value())
            {
                is_event_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsEventPresent(L"Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource", L"EventReceived");
            }

            if (!is_event_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "event is not available in this version of Windows");
                return nullptr;
            }

            auto param0 = py::convert_to<winrt::Windows::Foundation::TypedEventHandler<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource, winrt::Windows::System::Implementation::FileExplorer::SysStorageProviderEventReceivedEventArgs>>(arg);

            return py::convert(self->obj.EventReceived(param0));
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* ISysStorageProviderEventSource_remove_EventReceived(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource* self, PyObject* arg) noexcept
    {
        try
        {
            static std::optional<bool> is_event_present{};

            if (!is_event_present.has_value())
            {
                is_event_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsEventPresent(L"Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource", L"EventReceived");
            }

            if (!is_event_present.value())
            {
                PyErr_SetString(PyExc_AttributeError, "event is not available in this version of Windows");
                return nullptr;
            }

            auto param0 = py::convert_to<winrt::event_token>(arg);

            self->obj.EventReceived(param0);
            Py_RETURN_NONE;
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyObject* _assign_array_ISysStorageProviderEventSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_ISysStorageProviderEventSource(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ISysStorageProviderEventSource[] = {
        { "add_event_received", reinterpret_cast<PyCFunction>(ISysStorageProviderEventSource_add_EventReceived), METH_O, nullptr },
        { "remove_event_received", reinterpret_cast<PyCFunction>(ISysStorageProviderEventSource_remove_EventReceived), METH_O, nullptr },
        { "_assign_array_", _assign_array_ISysStorageProviderEventSource, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ISysStorageProviderEventSource), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ISysStorageProviderEventSource[] = {
        { }
    };

    static PyType_Slot _type_slots_ISysStorageProviderEventSource[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_ISysStorageProviderEventSource) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_ISysStorageProviderEventSource) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_ISysStorageProviderEventSource) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_ISysStorageProviderEventSource) },
        { }
    };

    static PyType_Spec type_spec_ISysStorageProviderEventSource = {
        "winrt._winrt_windows_system_implementation_fileexplorer.ISysStorageProviderEventSource",
        sizeof(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderEventSource),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ISysStorageProviderEventSource};

    // ----- ISysStorageProviderHandlerFactory interface --------------------

    static PyObject* _new_ISysStorageProviderHandlerFactory(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory>::type_name);
        return nullptr;
    }

    static void _dealloc_ISysStorageProviderHandlerFactory(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* ISysStorageProviderHandlerFactory_GetEventSource(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 2)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.System.Implementation.FileExplorer.ISysStorageProviderHandlerFactory", L"GetEventSource", 2);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(2);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);
                auto param1 = py::convert_to<winrt::hstring>(args, 1);

                return py::convert(self->obj.GetEventSource(param0, param1));
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

    static PyObject* ISysStorageProviderHandlerFactory_GetHttpRequestProvider(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.System.Implementation.FileExplorer.ISysStorageProviderHandlerFactory", L"GetHttpRequestProvider", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::hstring>(args, 0);

                return py::convert(self->obj.GetHttpRequestProvider(param0));
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

    static PyObject* _assign_array_ISysStorageProviderHandlerFactory(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_ISysStorageProviderHandlerFactory(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ISysStorageProviderHandlerFactory[] = {
        { "get_event_source", reinterpret_cast<PyCFunction>(ISysStorageProviderHandlerFactory_GetEventSource), METH_VARARGS, nullptr },
        { "get_http_request_provider", reinterpret_cast<PyCFunction>(ISysStorageProviderHandlerFactory_GetHttpRequestProvider), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_ISysStorageProviderHandlerFactory, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ISysStorageProviderHandlerFactory), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ISysStorageProviderHandlerFactory[] = {
        { }
    };

    static PyType_Slot _type_slots_ISysStorageProviderHandlerFactory[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_ISysStorageProviderHandlerFactory) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_ISysStorageProviderHandlerFactory) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_ISysStorageProviderHandlerFactory) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_ISysStorageProviderHandlerFactory) },
        { }
    };

    static PyType_Spec type_spec_ISysStorageProviderHandlerFactory = {
        "winrt._winrt_windows_system_implementation_fileexplorer.ISysStorageProviderHandlerFactory",
        sizeof(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHandlerFactory),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ISysStorageProviderHandlerFactory};

    // ----- ISysStorageProviderHttpRequestProvider interface --------------------

    static PyObject* _new_ISysStorageProviderHttpRequestProvider(PyTypeObject* /*unused*/, PyObject* /*unused*/, PyObject* /*unused*/) noexcept
    {
        static_assert(py::py_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider>::type_name);
        py::set_invalid_activation_error(py::py_type<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider>::type_name);
        return nullptr;
    }

    static void _dealloc_ISysStorageProviderHttpRequestProvider(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider* self) noexcept
    {
        auto tp = Py_TYPE(self);
        std::destroy_at(&self->obj);
        tp->tp_free(self);
        Py_DECREF(tp);
    }

    static PyObject* ISysStorageProviderHttpRequestProvider_SendRequestAsync(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider* self, PyObject* args) noexcept
    {
        auto arg_count = PyTuple_Size(args);

        if (arg_count == 1)
        {
            try
            {
                static std::optional<bool> is_overload_present{};

                if (!is_overload_present.has_value())
                {
                    is_overload_present = winrt::Windows::Foundation::Metadata::ApiInformation::IsMethodPresent(L"Windows.System.Implementation.FileExplorer.ISysStorageProviderHttpRequestProvider", L"SendRequestAsync", 1);
                }

                if (!is_overload_present.value())
                {
                    py::set_arg_count_version_error(1);
                    return nullptr;
                }

                auto param0 = py::convert_to<winrt::Windows::Web::Http::HttpRequestMessage>(args, 0);

                return py::convert(self->obj.SendRequestAsync(param0));
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

    static PyObject* _assign_array_ISysStorageProviderHttpRequestProvider(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        auto array = std::make_unique<py::ComArray<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider>>();
        if (!py::cpp::_winrt::Array_Assign(arg, std::move(array)))
        {
            return nullptr;
        }
        Py_RETURN_NONE;
    }

    static PyObject* _from_ISysStorageProviderHttpRequestProvider(PyObject* /*unused*/, PyObject* arg) noexcept
    {
        try
        {
            auto return_value = py::convert_to<winrt::Windows::Foundation::IInspectable>(arg);
            return py::convert(return_value.as<winrt::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider>());
        }
        catch (...)
        {
            py::to_PyErr();
            return nullptr;
        }
    }

    static PyMethodDef _methods_ISysStorageProviderHttpRequestProvider[] = {
        { "send_request_async", reinterpret_cast<PyCFunction>(ISysStorageProviderHttpRequestProvider_SendRequestAsync), METH_VARARGS, nullptr },
        { "_assign_array_", _assign_array_ISysStorageProviderHttpRequestProvider, METH_O | METH_STATIC, nullptr },
        { "_from", reinterpret_cast<PyCFunction>(_from_ISysStorageProviderHttpRequestProvider), METH_O | METH_STATIC, nullptr },
        { }
    };

    static PyGetSetDef _getset_ISysStorageProviderHttpRequestProvider[] = {
        { }
    };

    static PyType_Slot _type_slots_ISysStorageProviderHttpRequestProvider[] = {
        { Py_tp_new, reinterpret_cast<void*>(_new_ISysStorageProviderHttpRequestProvider) },
        { Py_tp_dealloc, reinterpret_cast<void*>(_dealloc_ISysStorageProviderHttpRequestProvider) },
        { Py_tp_methods, reinterpret_cast<void*>(_methods_ISysStorageProviderHttpRequestProvider) },
        { Py_tp_getset, reinterpret_cast<void*>(_getset_ISysStorageProviderHttpRequestProvider) },
        { }
    };

    static PyType_Spec type_spec_ISysStorageProviderHttpRequestProvider = {
        "winrt._winrt_windows_system_implementation_fileexplorer.ISysStorageProviderHttpRequestProvider",
        sizeof(py::wrapper::Windows::System::Implementation::FileExplorer::ISysStorageProviderHttpRequestProvider),
        0,
        Py_TPFLAGS_DEFAULT,
        _type_slots_ISysStorageProviderHttpRequestProvider};

    // ----- Windows.System.Implementation.FileExplorer Initialization --------------------

    PyDoc_STRVAR(module_doc, "Windows.System.Implementation.FileExplorer");

    static PyModuleDef module_def = {
        PyModuleDef_HEAD_INIT,
        "_winrt_windows_system_implementation_fileexplorer",
        module_doc,
        0,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
        nullptr};
} // py::cpp::Windows::System::Implementation::FileExplorer

PyMODINIT_FUNC PyInit__winrt_windows_system_implementation_fileexplorer(void) noexcept
{
    using namespace py::cpp::Windows::System::Implementation::FileExplorer;

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

    py::pytype_handle SysStorageProviderEventReceivedEventArgs_type{py::register_python_type(module.get(), &type_spec_SysStorageProviderEventReceivedEventArgs, object_bases.get(), nullptr)};
    if (!SysStorageProviderEventReceivedEventArgs_type)
    {
        return nullptr;
    }

    py::pytype_handle ISysStorageProviderEventSource_type{py::register_python_type(module.get(), &type_spec_ISysStorageProviderEventSource, object_bases.get(), nullptr)};
    if (!ISysStorageProviderEventSource_type)
    {
        return nullptr;
    }

    py::pytype_handle ISysStorageProviderHandlerFactory_type{py::register_python_type(module.get(), &type_spec_ISysStorageProviderHandlerFactory, object_bases.get(), nullptr)};
    if (!ISysStorageProviderHandlerFactory_type)
    {
        return nullptr;
    }

    py::pytype_handle ISysStorageProviderHttpRequestProvider_type{py::register_python_type(module.get(), &type_spec_ISysStorageProviderHttpRequestProvider, object_bases.get(), nullptr)};
    if (!ISysStorageProviderHttpRequestProvider_type)
    {
        return nullptr;
    }


    return module.detach();
}
