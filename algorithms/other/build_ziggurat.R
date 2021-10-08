build_ziggurat <- function(n) {
  
  ziggurat <- matrix(0, nrow=n+(n-1), ncol=n+(n-1))
  for (i in 1:n) {
    ziggurat[i:(n+(n-i)), i:(n+(n-i))] <- i
  }
  return (ziggurat)
  }
  

build_ziggurat(as.numeric(readline(prompt = "")))
