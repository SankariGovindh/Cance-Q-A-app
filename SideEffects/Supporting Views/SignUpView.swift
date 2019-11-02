//
//  SignUpView.swift
//  SideEffects
//
//  Created by Kevin Tran on 10/28/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct SignUpView: View {
    @State private var showingAlert = false
    @Environment(\.presentationMode) var mode: Binding<PresentationMode>
    @State private var selection: Int? = nil
    @EnvironmentObject var signupData: SignupData
    @State private var networkManager = NetworkManager()
    var body: some View {
       VStack {
        Text("New User").font(Font.system(size: 60, design: .default))
           
           HStack {
               Text("First Name")
            TextField("First Name", text: $signupData.firstname, onEditingChanged: { isEditing in }).foregroundColor(.primary).padding().textFieldStyle(RoundedBorderTextFieldStyle())

               Button(action: {
                self.signupData.firstname = ""
               }) {
                Image(systemName: "xmark.circle.fill").opacity(signupData.firstname == "" ? 0 : 1)
               }
           }.padding().offset(y:10)
           
           HStack {
               Text("Last Name")
            TextField("Last Name", text: $signupData.lastname, onEditingChanged: { isEditing in
                   }).foregroundColor(.primary).padding().textFieldStyle(RoundedBorderTextFieldStyle())

               Button(action: {
                self.signupData.lastname = ""
               }) {
                Image(systemName: "xmark.circle.fill").opacity(signupData.lastname == "" ? 0 : 1)
               }
           }.padding().offset(y:-10)
        
            HStack {
            Text("Username")
                TextField("Username", text: $signupData.username, onEditingChanged: { isEditing in
                    }).foregroundColor(.primary).padding()  .textFieldStyle(RoundedBorderTextFieldStyle())

                Button(action: {
                    self.signupData.username = ""
                }) {
                    Image(systemName: "xmark.circle.fill").opacity(signupData.username == "" ? 0 : 1)
                }
            }.padding().offset(y:-20)
        
            HStack {
            Text("Password")
                TextField("Password", text: $signupData.password, onEditingChanged: { isEditing in
                    }).foregroundColor(.primary).padding()  .textFieldStyle(RoundedBorderTextFieldStyle())

                Button(action: {
                    self.signupData.password = ""
                }) {
                    Image(systemName: "xmark.circle.fill").opacity(signupData.password == "" ? 0 : 1)
                }
            }.padding().offset(y:-30)
        
            HStack {
            Text("Email")
                TextField("Email", text: $signupData.email, onEditingChanged: { isEditing in
                    }).foregroundColor(.primary).padding()  .textFieldStyle(RoundedBorderTextFieldStyle())

                Button(action: {
                    self.signupData.email = ""
                }) {
                    Image(systemName: "xmark.circle.fill").opacity(signupData.email == "" ? 0 : 1)
                }
            }.padding().offset(y:-40)
        
            Button(action: {
                if self.signupData.validate() {
                    if self.networkManager.post(code: 2, uploadData: self.signupData.create_keys_values()) {
                        self.signupData.firstname = ""
                        self.signupData.lastname = ""
                        self.signupData.username = ""
                        self.signupData.password = ""
                        self.signupData.email = ""
                        self.showingAlert = true
                    }
                }
                self.mode.wrappedValue.dismiss()})
            {
                Text("Submit")
                    .padding()
                    .foregroundColor(.white)
                    .background(LinearGradient(gradient: Gradient(colors: [Color.red,  Color.purple]), startPoint: .leading, endPoint: .trailing))
                    .cornerRadius(40)
            }.alert(isPresented: $showingAlert) {
                Alert(title: Text("Account"), message: Text("Created Successfully"), dismissButton: .default(Text("Okay")))
            }
            /*
            NavigationLink(destination: LoginView(), tag: 1, selection: $selection) {
                Button(action: {
                    print(self.signupData.password)
                    self.selection = 1
                    // self.loginData.password
                    // self.loginData.username
                }) {
                    Text("Submit")
                        .padding()
                        .foregroundColor(.white)
                        .background(LinearGradient(gradient: Gradient(colors: [Color.green,  Color.blue]), startPoint: .leading, endPoint: .trailing))
                        .cornerRadius(40)
                }
            }
            */
       }
    }
}

struct SignUpView_Previews: PreviewProvider {
    static var previews: some View {
        SignUpView()
    }
}
