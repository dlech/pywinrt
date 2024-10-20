// WARNING: Please don't edit this file. It was generated by Python/WinRT v0.0.0

#pragma once

#include "pybase.h"
static_assert(winrt::check_version(PYWINRT_VERSION, "0.0.0"), "Mismatched Py/WinRT headers.");

#if __has_include("py.Windows.Foundation.h")
#include "py.Windows.Foundation.h"
#endif

#if __has_include("py.Windows.Foundation.Collections.h")
#include "py.Windows.Foundation.Collections.h"
#endif

#if __has_include("py.Windows.Graphics.Display.h")
#include "py.Windows.Graphics.Display.h"
#endif

#include <winrt/Windows.Foundation.h>
#include <winrt/Windows.Foundation.Collections.h>
#include <winrt/Windows.Graphics.Display.h>

#include <winrt/Windows.Devices.Sensors.h>

namespace py::proj::Windows::Devices::Sensors
{}

namespace py::impl::Windows::Devices::Sensors
{}

namespace py::wrapper::Windows::Devices::Sensors
{
    using Accelerometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Accelerometer>;
    using AccelerometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerDataThreshold>;
    using AccelerometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerReading>;
    using AccelerometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerReadingChangedEventArgs>;
    using AccelerometerShakenEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AccelerometerShakenEventArgs>;
    using ActivitySensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensor>;
    using ActivitySensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorReading>;
    using ActivitySensorReadingChangeReport = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangeReport>;
    using ActivitySensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangedEventArgs>;
    using ActivitySensorTriggerDetails = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ActivitySensorTriggerDetails>;
    using AdaptiveDimmingOptions = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AdaptiveDimmingOptions>;
    using Altimeter = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Altimeter>;
    using AltimeterReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AltimeterReading>;
    using AltimeterReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::AltimeterReadingChangedEventArgs>;
    using Barometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Barometer>;
    using BarometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::BarometerDataThreshold>;
    using BarometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::BarometerReading>;
    using BarometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::BarometerReadingChangedEventArgs>;
    using Compass = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Compass>;
    using CompassDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::CompassDataThreshold>;
    using CompassReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::CompassReading>;
    using CompassReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::CompassReadingChangedEventArgs>;
    using Gyrometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Gyrometer>;
    using GyrometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::GyrometerDataThreshold>;
    using GyrometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::GyrometerReading>;
    using GyrometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::GyrometerReadingChangedEventArgs>;
    using HingeAngleReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HingeAngleReading>;
    using HingeAngleSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HingeAngleSensor>;
    using HingeAngleSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HingeAngleSensorReadingChangedEventArgs>;
    using HumanPresenceFeatures = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HumanPresenceFeatures>;
    using HumanPresenceSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HumanPresenceSensor>;
    using HumanPresenceSensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HumanPresenceSensorReading>;
    using HumanPresenceSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HumanPresenceSensorReadingChangedEventArgs>;
    using HumanPresenceSensorReadingUpdate = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HumanPresenceSensorReadingUpdate>;
    using HumanPresenceSettings = py::winrt_wrapper<winrt::Windows::Devices::Sensors::HumanPresenceSettings>;
    using Inclinometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Inclinometer>;
    using InclinometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::InclinometerDataThreshold>;
    using InclinometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::InclinometerReading>;
    using InclinometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::InclinometerReadingChangedEventArgs>;
    using LightSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensor>;
    using LightSensorDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensorDataThreshold>;
    using LightSensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensorReading>;
    using LightSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LightSensorReadingChangedEventArgs>;
    using LockOnLeaveOptions = py::winrt_wrapper<winrt::Windows::Devices::Sensors::LockOnLeaveOptions>;
    using Magnetometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Magnetometer>;
    using MagnetometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::MagnetometerDataThreshold>;
    using MagnetometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::MagnetometerReading>;
    using MagnetometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::MagnetometerReadingChangedEventArgs>;
    using OrientationSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::OrientationSensor>;
    using OrientationSensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::OrientationSensorReading>;
    using OrientationSensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::OrientationSensorReadingChangedEventArgs>;
    using Pedometer = py::winrt_wrapper<winrt::Windows::Devices::Sensors::Pedometer>;
    using PedometerDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::PedometerDataThreshold>;
    using PedometerReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::PedometerReading>;
    using PedometerReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::PedometerReadingChangedEventArgs>;
    using ProximitySensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensor>;
    using ProximitySensorDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorDataThreshold>;
    using ProximitySensorDisplayOnOffController = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorDisplayOnOffController>;
    using ProximitySensorReading = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorReading>;
    using ProximitySensorReadingChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ProximitySensorReadingChangedEventArgs>;
    using SensorDataThresholdTriggerDetails = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SensorDataThresholdTriggerDetails>;
    using SensorQuaternion = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SensorQuaternion>;
    using SensorRotationMatrix = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SensorRotationMatrix>;
    using SimpleOrientationSensor = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SimpleOrientationSensor>;
    using SimpleOrientationSensorOrientationChangedEventArgs = py::winrt_wrapper<winrt::Windows::Devices::Sensors::SimpleOrientationSensorOrientationChangedEventArgs>;
    using WakeOnApproachOptions = py::winrt_wrapper<winrt::Windows::Devices::Sensors::WakeOnApproachOptions>;
    using IHumanPresenceSensorExtension = py::winrt_wrapper<winrt::Windows::Devices::Sensors::IHumanPresenceSensorExtension>;
    using ISensorDataThreshold = py::winrt_wrapper<winrt::Windows::Devices::Sensors::ISensorDataThreshold>;
}

namespace py
{
    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::AccelerometerReadingType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::ActivitySensorReadingConfidence> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::ActivityType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::HumanEngagement> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::HumanPresence> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::MagnetometerAccuracy> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::PedometerStepKind> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::SensorOptimizationGoal> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::SensorReadingType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::SensorType> = "i";

    template<>
    inline constexpr const char* buffer_format<winrt::Windows::Devices::Sensors::SimpleOrientation> = "i";


    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AccelerometerReadingType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AccelerometerReadingType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivitySensorReadingConfidence>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivitySensorReadingConfidence";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivityType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivityType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanEngagement>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanEngagement";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresence>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresence";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::MagnetometerAccuracy>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "MagnetometerAccuracy";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::PedometerStepKind>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "PedometerStepKind";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SensorOptimizationGoal>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SensorOptimizationGoal";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SensorReadingType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SensorReadingType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SensorType>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SensorType";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SimpleOrientation>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SimpleOrientation";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Accelerometer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Accelerometer";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AccelerometerDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AccelerometerDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AccelerometerReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AccelerometerReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AccelerometerReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AccelerometerReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AccelerometerShakenEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AccelerometerShakenEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivitySensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivitySensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivitySensorReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivitySensorReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangeReport>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivitySensorReadingChangeReport";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivitySensorReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivitySensorReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ActivitySensorTriggerDetails>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ActivitySensorTriggerDetails";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AdaptiveDimmingOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AdaptiveDimmingOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Altimeter>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Altimeter";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AltimeterReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AltimeterReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::AltimeterReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "AltimeterReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Barometer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Barometer";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::BarometerDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "BarometerDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::BarometerReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "BarometerReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::BarometerReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "BarometerReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Compass>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Compass";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::CompassDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "CompassDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::CompassReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "CompassReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::CompassReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "CompassReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Gyrometer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Gyrometer";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::GyrometerDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "GyrometerDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::GyrometerReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "GyrometerReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::GyrometerReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "GyrometerReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HingeAngleReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HingeAngleReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HingeAngleSensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HingeAngleSensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HingeAngleSensorReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HingeAngleSensorReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresenceFeatures>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresenceFeatures";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresenceSensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresenceSensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresenceSensorReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresenceSensorReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresenceSensorReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresenceSensorReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresenceSensorReadingUpdate>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresenceSensorReadingUpdate";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::HumanPresenceSettings>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "HumanPresenceSettings";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Inclinometer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Inclinometer";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::InclinometerDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "InclinometerDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::InclinometerReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "InclinometerReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::InclinometerReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "InclinometerReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::LightSensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "LightSensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::LightSensorDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "LightSensorDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::LightSensorReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "LightSensorReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::LightSensorReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "LightSensorReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::LockOnLeaveOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "LockOnLeaveOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Magnetometer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Magnetometer";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::MagnetometerDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "MagnetometerDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::MagnetometerReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "MagnetometerReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::MagnetometerReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "MagnetometerReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::OrientationSensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "OrientationSensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::OrientationSensorReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "OrientationSensorReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::OrientationSensorReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "OrientationSensorReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::Pedometer>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "Pedometer";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::PedometerDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "PedometerDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::PedometerReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "PedometerReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::PedometerReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "PedometerReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ProximitySensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ProximitySensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ProximitySensorDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ProximitySensorDataThreshold";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ProximitySensorDisplayOnOffController>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ProximitySensorDisplayOnOffController";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ProximitySensorReading>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ProximitySensorReading";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ProximitySensorReadingChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ProximitySensorReadingChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SensorDataThresholdTriggerDetails>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SensorDataThresholdTriggerDetails";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SensorQuaternion>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SensorQuaternion";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SensorRotationMatrix>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SensorRotationMatrix";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SimpleOrientationSensor>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SimpleOrientationSensor";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::SimpleOrientationSensorOrientationChangedEventArgs>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "SimpleOrientationSensorOrientationChangedEventArgs";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::WakeOnApproachOptions>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "WakeOnApproachOptions";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::IHumanPresenceSensorExtension>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "IHumanPresenceSensorExtension";
    };

    template<>
    struct py_type<winrt::Windows::Devices::Sensors::ISensorDataThreshold>
    {
        static constexpr const char* module_name = "winrt.windows.devices.sensors";
        static constexpr const char* type_name = "ISensorDataThreshold";
    };
}
