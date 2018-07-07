__all__ = [
    # new:
    'UpdateTimeSteps',
    'GetRequestedTime',
    'GetInputTimeSteps',
]

import numpy as np



def _calculateTimeRange(nt, dt=1.0):
    """
    desc: Discretizes time range accoridng to step size `dt` in seconds
    """
    return np.arange(0,nt*dt,dt, dtype=float)



def UpdateTimeSteps(algorithm, nt, dt):
    """@desc: Handles setting up the timesteps on on the pipeline for a file series reader.

    @params:
    algorithm : vtkDataObject : req : The data object (Proxy) on the pipeline (pass `self` from algorithm subclasses)
    nt : int or list : req : Number of timesteps (Pass a list to use length of that list)
    dt : float : optional : The discrete value in seconds for the time step.

    @return:
    np.array : Returns the timesteps
    """
    if isinstance(nt, list):
        nt = len(nt)
    executive = algorithm.GetExecutive()
    oi = executive.GetOutputInformation(0)
    #oi = outInfo.GetInformationObject(0)
    oi.Remove(executive.TIME_STEPS())
    oi.Remove(executive.TIME_RANGE())
    timesteps = _calculateTimeRange(nt, dt=1.0)
    for t in timesteps:
        oi.Append(executive.TIME_STEPS(), t)
    oi.Append(executive.TIME_RANGE(), timesteps[0])
    oi.Append(executive.TIME_RANGE(), timesteps[-1])
    return timesteps

def GetRequestedTime(algorithm, outInfoVec, idx=0):
    """@desc: Handles setting up the timesteps on on the pipeline for a file series reader.

    @params:
    algorithm : vtkDataObject : req : The data object (Proxy) on the pipeline (pass `self` from algorithm subclasses)
    outInfoVec : vtkInformationVector : The output information for the algorithm
    idx : int : optional : the index for the output port

    @return:
    int : the index of the requested time

    @notes:
    ```py
    # Get requested time index
    i = _helpers.GetRequestedTime(self, outInfoVec)
    ```
    """
    executive = algorithm.GetExecutive()
    timesteps = algorithm.GetTimestepValues()
    outInfo = outInfoVec.GetInformationObject(idx)
    if timesteps is None or len(timesteps) == 0:
        return 0
    elif outInfo.Has(executive.UPDATE_TIME_STEP()) and len(timesteps) > 0:
        utime = outInfo.Get(executive.UPDATE_TIME_STEP())
        return np.argmin(np.abs(np.array(timesteps) - utime))
    else:
        # if we cant match the time, give first
        assert(len(timesteps) > 0)
        return 0

def GetInputTimeSteps(algorithm, port=0, idx=0):
    """@desc: Get the timestep values for the algorithm's input

    @params:
    algorithm : vtkDataObject : req : The data object (Proxy) on the pipeline (pass `self` from algorithm subclasses)
    port : int : optional : the input port
    idx : int : optional : the connection index on the input port

    @return:
    list : the time step values of the input
    """
    executive = algorithm.GetExecutive()
    ii = executive.GetInputInformation(port, idx)
    return ii.Get(executive.TIME_STEPS())
