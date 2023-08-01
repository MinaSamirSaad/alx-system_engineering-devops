#!/usr/bin/env ruby
puts ARGV[0].scan(/
(?:from:)(?<sender>[^\]]*) # sender
(?:.*to:)(?<receiver>[^\]]*) # receiver
(?:.*flags:)(?<flags>[^\]]*)  # flags
/x).join(",")
