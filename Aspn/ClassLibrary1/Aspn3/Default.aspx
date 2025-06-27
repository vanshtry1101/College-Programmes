<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <asp:Label ID="Label1" runat="server" Text="Enter First Name"></asp:Label>
        <asp:TextBox ID="TextBox1" runat="server" AutoCompleteType="FirstName"></asp:TextBox>
        <br />
        <asp:Label ID="Label2" runat="server" Text="Enter Last Name"></asp:Label>
        <asp:TextBox ID="TextBox2" runat="server" AutoCompleteType="LastName"></asp:TextBox>
        <br />
        <asp:Label ID="Label3" runat="server" Text="Enter Mail"></asp:Label>
        <asp:TextBox ID="TextBox3" runat="server" AutoCompleteType="Email"></asp:TextBox>
        <br />
        <asp:Label ID="Label4" runat="server" Text="Enter Mobile"></asp:Label>
        <asp:TextBox ID="TextBox4" runat="server" AutoCompleteType="BusinessPhone"></asp:TextBox>
        <br />
        <asp:Button ID="Button1" runat="server" OnClientClick="alert('Client side Click')" PostBackUrl="~/Default2.aspx" Text="Next Page" />
    </form>
</body>
</html>
