<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default2.aspx.cs" Inherits="Default2" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            Enter First Name<asp:TextBox ID="TextBox5" runat="server" AutoCompleteType="FirstName"></asp:TextBox>
            <br />
            Enter Last Name<asp:TextBox ID="TextBox6" runat="server" AutoCompleteType="LastName"></asp:TextBox>
            <br />
            Enter Emil
            <asp:TextBox ID="TextBox7" runat="server" AutoCompleteType="Email"></asp:TextBox>
            <br />
            Enter Phone
            <asp:TextBox ID="TextBox8" runat="server" AutoCompleteType="BusinessPhone"></asp:TextBox>
            <br />
            <asp:Button ID="Button1" runat="server" PostBackUrl="~/Default.aspx" Text="Previous Page" />
        </div>
    </form>
</body>
</html>
