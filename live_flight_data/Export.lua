function LuaExportStart()
  -- Open file for writing
  file = io.open("C:/Users/acada/Documents/F14-FBW/input_output/telemetry.csv", "w")
  assert(file ~= nil, "Could not open file for writing")
  
  -- Write header row to file
  file:write("Time,Lat,Long,Heading,Baralt,Radalt,Pitch,Bank,Yaw,IAS,TAS,Gx,Gy,Gz,AOA,VS\n")
end

function LuaExportAfterNextFrame()
  -- Get telemetry data
  local time = LoGetModelTime()
  local selfdata = LoGetSelfData()
  local lat = selfdata.LatLongAlt.Lat
  local long = selfdata.LatLongAlt.Long
  local heading = selfdata.Heading
  local baralt = LoGetAltitudeAboveSeaLevel()
  local radalt = LoGetAltitudeAboveGroundLevel()
  local pitch, bank, yaw = LoGetADIPitchBankYaw()
  local ias = LoGetIndicatedAirSpeed()
  local tas = LoGetTrueAirSpeed()
  local g = LoGetAccelerationUnits()
  local gx = g.x
  local gy = g.y
  local gz = g.z
  local aoa = LoGetAngleOfAttack()
  local vs = LoGetVerticalVelocity()

  -- Write telemetry data to file
  file:write(string.format("%.2f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
      time, lat, long, heading, baralt, radalt, pitch, bank, yaw, ias, tas, gx, gy, gz, aoa, vs))
end

function LuaExportStop()
  -- Close file
  if file ~= nil then
      file:close()
  end
end