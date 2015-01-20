#
# motors/pololu/qik2s9v1.py
#
# Usual device on Linux: /dev/ttyUSB0
#

"""
This code was written to work with the Pololu Qik 2s9v1 motor controller.
http://www.pololu.com/catalog/product/1110

by Carl J. Nobile

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
__docformat__ = "restructuredtext en"


from .qik import Qik

__version__ = '1.0.0'
__version_info__ = tuple([ int(num) for num in __version__.split('.')])


class Qik2s9v1(Qik):
    QIK_VER_1 = 1
    QIK_VER_2 = 2
    _DEFAULT_DEVICE_ID = 0x09
    _COMMAND = {
        'get-fw-version': 0x01,
        'get-error': 0x02,
        'get-config': 0x03,
        'set-config': 0x04,
        'm0-coast': 0x06,
        'm1-coast': 0x07,
        'm0-forward-7bit': 0x08,
        'm0-forward-8bit': 0x09,
        'm0-reverse-7bit': 0x0A,
        'm0-reverse-8bit': 0x0B,
        'm1-forward-7bit': 0x0C,
        'm1-forward-8bit': 0x0D,
        'm1-reverse-7bit': 0x0E,
        'm1-reverse-8bit': 0x0F,
       }
    _ERRORS = {
        0: 'OK',
        1: 'Bit 0 Unused',
        2: 'Bit 1 Unused',
        4: 'Bit 2 Unused',
        8: 'Data Overrun Error',
        16: 'Frame Error',
        32: 'CRC Error',
        64: 'Format Error',
        128: 'Timeout',
        }
    DEVICE_ID = 0x00
    PWM_PARAM = 0x01
    MOTOR_ERR_SHUTDOWN = 0x02
    SERIAL_TIMEOUT = 0x03
    _CONFIG_NUM = {
        DEVICE_ID: 'Device ID',
        PWM_PARAM: 'PWM Parameter',
        MOTOR_ERR_SHUTDOWN: 'Shutdown Motors on Error',
        SERIAL_TIMEOUT: 'Serial Error',
        }
    _CONFIG_PWM = {
        0: (31500, '7-Bit, PWM Frequency 31.5kHz'),
        1: (15700, '8-Bit, PWM Frequency 15.7 kHz'),
        2: (7800, '7-Bit, PWM Frequency 7.8 kHz'),
        3: (3900, '8-Bit, PWM Frequency 3.9 kHz'),
        }
    _CONFIG_PWM_TO_VALUE = dict([(v[0], k) for k, v in _CONFIG_PWM.items()])
    MOTORS_CONTINUE = 0
    MOTORS_STOPPED = 1
    _CONFIG_MOTOR = {
        MOTORS_CONTINUE: 'Motors are not stopped on error.',
        MOTORS_STOPPED: 'Motors are stopped on error.',
        }

    def __init__(self, device, baud=38400, version=QIK_VER_2,
                 readTimeout=None, writeTimeout=None, log=None):
        super(Qik2s9v1, self).__init__(device, baud, version, readTimeout,
                                       writeTimeout, log)
        self._timeoutToValue = self._genTimeoutList(0.262)
        self.findConnectedDevices()

    def getFirmwareVersion(self, device=_DEFAULT_DEVICE_ID):
        """
        Get the firmware version of the Qik 2s9v1 hardware.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Returns:
          An integer indicating the version number.
        """
        return self._getFirmwareVersion(device)

    def getError(self, device=_DEFAULT_DEVICE_ID, message=True):
        """
        Get the error message or value stored in the Qik 2s9v1 hardware.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.
          message : `bool`
            If set to `True` a text message will be returned, if set to `False`
            the integer stored in the Qik will be returned.

        :Returns:
          A text message or an int. See the `message` parameter above.
        """
        return self._getError(device, message)

    def getDeviceID(self, device=_DEFAULT_DEVICE_ID):
        """
        Get the device ID.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Returns:
          An integer number of the hardware device ID.
        """
        return self._getDeviceID(device)

    def getPWMFrequency(self, device=_DEFAULT_DEVICE_ID, message=True):
        """
        Get the motor shutdown on error status stored on the hardware device.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.
          message : `bool`
            If set to `True` a text message will be returned, if set to `False`
            the integer stored in the Qik will be returned.

        :Returns:
          A text message or an int. See the `message` parameter above.
        """
        return self._getPWMFrequency(device, message)

    def getMotorShutdown(self, device=_DEFAULT_DEVICE_ID):
        """
        Get the motor shutdown on error status stored on the hardware device.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Returns:
          Text message indicating the status of the shutdown error.
        """
        return self._getMotorShutdown(device)

    def getSerialTimeout(self, device=_DEFAULT_DEVICE_ID):
        """
        Get the serial timeout stored on the hardware device.

        Caution, more that one value returned from the Qik can have the same
        actual timeout value according the the formula below. I have verified
        this as an idiosyncrasy of the Qik itself. There are only a total of
        72 unique values that the Qik can logically use the remaining 56
        values are repeats of the 72.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Returns:
          The timeout value in seconds.
        """
        return self._getSerialTimeout(device)

    def setDeviceID(self, value, device=_DEFAULT_DEVICE_ID, message=True):
        """
        Set the hardware device number. This is only needed if more that one
        device is on the same serial buss.

        :Parameters:
          value : `int`
            The device ID to set in the range of 0 - 127.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.
          message : `bool`
            If set to `True` a text message will be returned, if set to `False`
            the integer stored in the Qik will be returned.

        :Returns:
          A text message or an int. See the `message` parameter above.

        :Exceptions:
          SerialException
            IO error indicating there was a problem reading from the serial
            connection.
        """
        return self._setDeviceID(value, device, message)

    def setPWMFrequency(self, pwm, device=_DEFAULT_DEVICE_ID, message=True):
        """
        Set the PWM frequency.

        :Parameters:
          pwm : `int`
            The PWN frequency to set in hertz.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.
          message : `bool`
            If set to `True` a text message will be returned, if set to `False`
            the integer stored in the Qik will be returned.

        :Returns:
          A text message or an int. See the `message` parameter above.

        :Exceptions:
          SerialException
            IO error indicating there was a problem reading from the serial
            connection.
        """
        return self._setPWMFrequency(pwm, device, message)

    def setMotorShutdown(self, value, device=_DEFAULT_DEVICE_ID, message=True):
        """
        Set the motor shutdown on error status stored on the hardware device.

        :Parameters:
          value : `int`
            An integer indicating the effect on the motors when an error occurs.
            A `1` will cause the cause the motors to stop on an error and a
            `0` will ignore errors keeping the motors running.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.
          message : `bool`
            If set to `True` a text message will be returned, if set to `False`
            the integer stored in the Qik will be returned.

        :Returns:
          Text message indicating the status of the shutdown error.
          A text message or an int. See the `message` parameter above.

        :Exceptions:
          SerialException
            IO error indicating there was a problem reading from the serial
            connection.
        """
        return self._setMotorShutdown(value, device, message)

    def setSerialTimeout(self, timeout, device=_DEFAULT_DEVICE_ID,
                         message=True):
        """
        Set the serial timeout on the hardware device.

        Setting the serial timeout to anything other than zero will cause an
        error if the serial line is inactive for the time set. This may not be
        a good thing as leaving the Qik idle may be a required event. Why
        would you want the Qik to report an error when none actually occurred
        and your Qik was just idle? This happens with or without the motors
        running.

        This also explains why if the Qik is set at a very low timeout that the
        red LED will come on almost immediately. You will not even get a chance
        to send it a command before the timeout. This would be like temporarily
        bricking your Qik. Not a good thing though it's easy to fix by just
        setting the timeout to 0 again.

        OK, so how do we actually use the serial timeout. Good question, the
        best way I can think of is to send the Qik a keep alive signal. One
        way of doing this is to execute the getError() method at a little less
        than half the timeout period. So if the timeout was set to 200ms you
        would get the error status every 90ms. The Qik will stay alive unless
        the keep alive signal is not seen. This should solve the problem, but
        getting the timing right may be an issue as different Qiks will timeout
        a little differently from others. When using more than one Qik on the
        serial buss this may become an issue. You will need to play with some
        different values.

        :Parameters:
          timeout : `float` or `int`
            The timeout value between 0 - 503.04 seconds, however, any number
            can be passed to the argument, the code will find the nearest
            allowed value from the 72 that are available.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.
          message : `bool`
            If set to `True` a text message will be returned, if set to `False`
            the integer stored in the Qik will be returned.

        :Returns:
          Text message indicating the status of the shutdown error.

        :Exceptions:
          SerialException
            IO error indicating there was a problem reading from the serial
            connection.
        """
        return self._setSerialTimeout(timeout, device, message)

    def setM0Coast(self, device=_DEFAULT_DEVICE_ID):
        """
        Set motor 0 to coast.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Exceptions:
          SerialTimeoutException
            If the low level serial package times out.
          SerialException
            IO error when the port is not open.
        """
        self._setM0Coast(device)

    def setM1Coast(self, device=_DEFAULT_DEVICE_ID):
        """
        Set motor 1 to coast.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Exceptions:
          SerialTimeoutException
            If the low level serial package times out.
          SerialException
            IO error when the port is not open.
        """
        self._setM1Coast(device)

    def setM0Speed(self, speed, device=_DEFAULT_DEVICE_ID):
        """
        Set motor 0 speed.

        :Parameters:
          speed : `int`
            Motor speed as an integer.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Exceptions:
          SerialTimeoutException
            If the low level serial package times out.
          SerialException
            IO error when the port is not open.
        """
        self._setM0Speed(speed, device)

    def setM1Speed(self, speed, device=_DEFAULT_DEVICE_ID):
        """
        Set motor 1 speed.

        :Parameters:
          speed : `int`
            Motor speed as an integer.

        :Keywords:
          device : `int`
            The device is the integer number of the hardware devices ID and
            is only used with the Pololu Protocol. Defaults to the hardware's
            default value.

        :Exceptions:
          SerialTimeoutException
            If the low level serial package times out.
          SerialException
            IO error when the port is not open.
        """
        self._setM1Speed(speed, device)