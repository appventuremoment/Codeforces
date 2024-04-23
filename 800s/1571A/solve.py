for _ in range(int(input())):
    string = input()
    if "><" in string.replace("=", "") or "<>" in string.replace("=", ""): print("?")
    elif ">" in string: print(">")
    elif "<" in string: print("<")
    else: print("=")


# Converted to kotlin through chatGPT

"""
fun main() {
    val n = readLine()!!.toInt()
    repeat(n) {
        val string = readLine()!!
        if ("><" in string.replace("=", "") || "<>" in string.replace("=", ""))
            println("?")
        else if (">" in string)
            println(">")
        else if ("<" in string)
            println("<")
        else
            println("=")
    }
}
"""