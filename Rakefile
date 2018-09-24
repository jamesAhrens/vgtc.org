task default: %w[test]

task :test do
  sh "git branch -a"
  sh "./build-on-travis.sh production"
end
