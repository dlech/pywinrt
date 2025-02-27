// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#include <winrt/Windows.Foundation.h>

#include <winrt/Microsoft.UI.Dispatching.h>

namespace py::proj::Microsoft::UI::Dispatching
{
}

namespace py::impl::Microsoft::UI::Dispatching
{
    struct DispatcherQueueHandler
    {
        static winrt::Microsoft::UI::Dispatching::DispatcherQueueHandler get(PyObject* callable)
        {
            py::delegate_callable _delegate{ callable };

            return [delegate = std::move(_delegate)]()
            {
                auto gil = py::ensure_gil();

                py::pyobj_handle args{ nullptr };
                py::pyobj_handle return_value{ PyObject_CallObject(delegate.callable(), args.get()) };

                if (!return_value)
                {
                    PyErr_WriteUnraisable(delegate.callable());
                    throw winrt::hresult_error();
                }
            };
        };
    };
}

namespace py::wrapper::Microsoft::UI::Dispatching
{
    using DispatcherExitDeferral = py::winrt_wrapper<winrt::Microsoft::UI::Dispatching::DispatcherExitDeferral>;
    using DispatcherQueue = py::winrt_wrapper<winrt::Microsoft::UI::Dispatching::DispatcherQueue>;
    using DispatcherQueueController = py::winrt_wrapper<winrt::Microsoft::UI::Dispatching::DispatcherQueueController>;
    using DispatcherQueueShutdownStartingEventArgs = py::winrt_wrapper<winrt::Microsoft::UI::Dispatching::DispatcherQueueShutdownStartingEventArgs>;
    using DispatcherQueueTimer = py::winrt_wrapper<winrt::Microsoft::UI::Dispatching::DispatcherQueueTimer>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::UI::Dispatching::DispatcherQueuePriority> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Microsoft::UI::Dispatching::DispatcherRunOptions> = "I";


    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherQueuePriority>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherQueuePriority";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherQueuePriority";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherRunOptions>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherRunOptions";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherRunOptions";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherExitDeferral>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherExitDeferral";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherExitDeferral";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherQueue>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherQueue";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherQueue";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherQueueController>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherQueueController";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherQueueController";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherQueueShutdownStartingEventArgs>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherQueueShutdownStartingEventArgs";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherQueueShutdownStartingEventArgs";
    };

    template<>
    struct py_type<winrt::Microsoft::UI::Dispatching::DispatcherQueueTimer>
    {
        static constexpr std::string_view qualified_name = "winrt.microsoft.ui.dispatching.DispatcherQueueTimer";
        static constexpr const char* module_name = "winrt.microsoft.ui.dispatching";
        static constexpr const char* type_name = "DispatcherQueueTimer";
    };
    template <>
    struct delegate_python_type<winrt::Microsoft::UI::Dispatching::DispatcherQueueHandler>
    {
        using type = py::impl::Microsoft::UI::Dispatching::DispatcherQueueHandler;
    };

}
