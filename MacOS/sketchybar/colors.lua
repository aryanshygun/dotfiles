return {
  black = 0x99000000,
  white = 0xffe2e2e3,
  red = 0xff6871FF,
  green = 0xff6871FF,
  blue = 0xff6871FF,
  yellow = 0xff6871FF,
  orange = 0xff6871FF,
  magenta = 0xff6871FF,
  grey = 0xffe2e2e3,
  purple = 0xff6871FF,
  transparent = 0x00000000,

  bar = {
    bg = 0xffffff,
    border = 0xff2c2e34,
  },
  popup = {
    bg = 0xc02c2e34,
    border = 0xff7f8490
  },
  bg1 = 0x55000000,
  bg2 = 0x55000000,
  blur1 = 0x55000000,
  blur2 = 0x99000000,

  with_alpha = function(color, alpha)
    if alpha > 1.0 or alpha < 0.0 then return color end
    return (color & 0x00ffffff) | (math.floor(alpha * 255.0) << 24)
  end,
}
