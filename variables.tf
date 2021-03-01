variable "keyName" {
  default = "blockchain-frontier-bot"
  type    = string
}

variable "keyPath" {
  default = "~/blockchain-frontier-bot.pem"
  type    = string
}

variable "dockerPass" {
  type = string
}

variable "dockerUser" {
  type = string
}