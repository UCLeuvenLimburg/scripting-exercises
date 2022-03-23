if ARGV.empty?
    n = 2
else
    n = ARGV[0].to_i
end

data = STDIN.gets.strip

n.times { puts data }